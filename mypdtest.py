# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 10:30:16 2019

@author: 10071616
"""

import numpy as np
import pandas as pd
import warnings; warnings.simplefilter('ignore') 
#忽略可能会出现的警告信息，警告并不是错误，可以忽略；

#--Series的构建和用法
# 通过list构建Series，list转换成为Series，用pd.Series;
df = pd.Series(range(10, 20))
print(type(df))
print (df.values ) #series其实是由Ndarry构成的；
print(df.head(5))
print(df[0])

# build series with dict
sales_data = {'a':1, 'b':2,'c':3}
df_dict = pd.Series(sales_data)

df.name = 'Series1'
df.index.name = 'Index'
df.head()

df = pd.Series(range(8,14), index = ['a', 'b', 'c', 'd', 'e','f'])

# DataFrame的构建
array = np.random.randn(6,4)
df = pd.DataFrame(array)               #通过Ndarray构建Dataframe,如果没有声明，默认的行index和列index都是从0开始；
df.head()

df = pd.DataFrame(np.random.randn(6,4), columns = ['a', 'b', 'c', 'd'], index = ['e','f','g','h','i','j'] )    #构建的时候明确了行和列的标签；

# 通过字典构建DataFrame
dict_data = {'Date': pd.datetime(2017,6,30),
             'Number': pd.Series([6,6,6]),
             'Course_name' : pd.Series(["Python","Quant","Finance","CFA"]),     #直接传一个list进去也是完全可以的；
             'Company' : 'JCAQF' }
# 显示DataFrame
df = pd.DataFrame(dict_data)
df.head()

# 自定义构建DataFrame
df = pd.DataFrame([10, 30, 60, 80], columns=['Quantity'],
                  index=['a', 'b', 'c', 'd'])

# 对DaraFram的选择操作

# 通过字典构建DataFrame
dict_data = {'Date': pd.datetime(2017,6,30),
             'Number': pd.Series([6, 6, 6, 6]),
             'Course_name' : pd.Series(["Python","Quant","Finance","CFA"]),     #直接传一个list进去也是完全可以的；
             'Company' : 'JCAQF' }

df = pd.DataFrame(dict_data)
df.head()

# 通过标签获取数据
#df[0]





