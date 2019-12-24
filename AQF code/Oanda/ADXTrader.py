# 声明：本资料仅供内部学习交流使用，切勿外传。金程教育
# AQF:Python ADX Strategy for Oanda v20
#

import v20
import numpy as np
import pandas as pd
import configparser
import talib

config = configparser.ConfigParser()
config.read('config.ini')

account_id = config['oanda']['account_id']
access_token = config['oanda']['api_key']


class ADXTrader():
    def __init__(self, instrument='XAU_USD', units=1, *args, **kwargs):

        self.ticks = 0
        self.position = 0                 #记录策略开仓方向
        self.account_id = account_id
        self.instrument = instrument
        self.units = units
        self.ctx = v20.Context(
            'api-fxpractice.oanda.com',
            443,
            True,
            application='sample_code',
            token=access_token,
            datetime_format='RFC3339'
        )
        self.ctx_stream = v20.Context(
            'stream-fxpractice.oanda.com',
            443,
            True,
            application='sample_code',
            token=access_token,
            datetime_format='RFC3339'
        )
        self.data = self._init_data(self.ctx)
        print(self.data.head(15))


    def _init_data(self, api, n_candles=28):
        '''取得过去28分钟的历史数据，用于初始化 self.data，拿历史数据计算指标节约策略执行时间；
            candle 结构：
            {'ask': {'c': '1.06163', 'h': '1.08765', 'l': '1.05983', 'o': '1.06163'},
             'complete': True,
             'time': '2016-12-07T22:01:00.000000000Z',
             'volume': 58060}
             '''
        close_dict = {}
        price_index = 'ohlc'
        res = api.instrument.candles(self.instrument, price='A', granularity='M1', count=n_candles)
        candles = [candle.dict() for candle in res.get('candles')]
        # print(candles)

        # 是对历史数据进行处理：Dict形式转换成为DataFrame形式；
        for candle in candles:
            for i in range(4):
                time = "%s%s%s" % (candle['time'][:18], str(i), candle['time'][-11:])
                close_dict[time] = float(candle['ask'][price_index[i]])
        result = pd.DataFrame(close_dict, index=['close']).T
        result.index = pd.DatetimeIndex(result.index)
        return result


    def create_order(self, units):  
        ''' 通过Oanda进行下单操作 '''
        reponse = self.ctx.order.market(
            self.account_id,
            instrument=self.instrument,
            units=units,
        )
        order = reponse.get('orderFillTransaction')
        print('\n\n', order.dict(), '\n')

    def close_orders(self):
        """ 关闭账户中的所有持仓"""
        if self.position == 1:  # 持有多头仓位
            request = self.ctx.position.close(self.account_id, self.instrument, longUnits='ALL')
            order = request.get('longOrderFillTransaction')
        elif self.position == -1:
            request = self.ctx.position.close(self.account_id, self.instrument, shortUnits='ALL')
            order = request.get('shortOrderFillTransaction')
        else:
            return
        
        print('\n\n', order.dict(), '\n')


    def start(self):
        ''' 开始获得实时数据 '''
        response = self.ctx_stream.pricing.stream(
            self.account_id,
            snapshot=True,
            instruments=self.instrument
        )
        for msg_type, msg in response.parts():
            if msg_type == 'pricing.Price':
                self.on_success(msg.time, msg.asks[0].price)
            if self.ticks >= 250:
                self.close_orders()
                return 'Finished.'

    def on_success(self, time, ask):
        ''' 实时数据处理策略逻辑：获得实时数据后的相关操作； 
            
        '''
        self.ticks += 1
        print(self.ticks, end=' ')
        self.data = self.data.append(
            pd.DataFrame({'close': [ask]}, index = pd.DatetimeIndex([time])))
        self.data.index.name = 'time'

        if self.ticks%10 == 0:       # 检查交易信号的频率；

            resam = self.data.resample('1min').last()

            resam['open'] = self.data.resample('1min').first()
            resam['high'] = self.data.resample('1min').max()
            resam['low'] = self.data.resample('1min').min()
            resam.dropna(inplace=True)

            high = resam['high'].values
            low = resam['low'].values
            close = resam['close'].values

            resam['ADX'] = talib.ADX(high, low, close, 14)
            resam['Plus_DI'] = talib.PLUS_DI(high, low, close, 14)
            resam['Minus_DI'] = talib.MINUS_DI(high, low, close, 14)

            resam['returns'] = np.sign(np.log(resam['close'] / resam['close'].shift(1)))

            # 持仓逻辑，当 ADX_Diff > 0 时，根据 DI 方向持仓，+DI > -DI,持有多头仓位，反之持有空头仓位，当ADX_Diff < 0 时空仓
            resam['ADX_Diff'] = np.sign(resam['ADX'].diff(1))

            # ADX_Diff < 0 时空仓
            resam.loc[resam['ADX_Diff'] < 1, 'ADX_Diff'] = 0

            # 计算+DI 与 -DI 关系
            resam['Direction'] = np.sign(resam['Plus_DI'] - resam['Minus_DI'])

            # 计算交易信号;
            resam['Position'] = resam['ADX_Diff'] * resam['Direction']

            if self.ticks > 249:
                print(resam)

            try:
                # 实时数据的处理逻辑；
                # 如果最新进来的信号是买入；
                # 新数据进来之后的处理逻辑：如果新信号是买入信号：
                # 若是空头，则先平仓，做多一单位；若是多头或空仓，则直接做多一单位
                if resam['Position'].ix[-1] == 1:
                    # 如果原来持有空头仓位，平掉空单，持有一单位多单
                    if self.position == -1:
                        self.close_orders()
                    # 如果原来空仓或持有多头仓，加仓一单位
                    self.create_order(self.units)
                    # 将持仓情况设置为持多仓
                    self.position = 1

                # 如果最新进来的信号是卖出
                elif resam['Position'].ix[-1] == -1:
                    # 如果原来持有多头仓位，平掉多头单，持有一单位空单
                    if self.position == 1:
                        self.close_orders()
                    self.create_order(-self.units)
                    self.position = -1

            # 为了防止这个时点上服务器没有tick数据传输过来，什么也不做，进行下一次数据的读取；
            except IndexError:
                pass


if __name__ == '__main__':

    trader = ADXTrader()
    trader.start()
