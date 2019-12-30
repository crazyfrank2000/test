# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 14:07:56 2019
My Numpy test code 

@author: 10071616
"""
#查看源代码：ctrl + 鼠标按键 或者 Ctrl+ G
#Run cell : ctrl + return
#Run cell and before : shift + return
#Run cell and after : Alt + return
"""
The basic data structure for python 
ndarray, list, tuple, dict,
"""

import numpy as np
my_arr = np.arange(1000)

my_tuple=(12,999,0.888)
tuple1=("abc","def")
tuple2=my_tuple+tuple1

print(my_tuple)

my_list = list(np.arange(100))
list1=[12,23,34]
list2=["asdfasdf","asdjfiasdf",list1,44]

list2.append(tuple2)
print(list2)

my_dict={'a':1,'b':2,'c':3}
print(my_dict.get('a'))
print(my_dict)

"""Now the numpy test code here 
The NumPy ndarray: A Multidimensional Array Object
key functions for ndarray
'ndarray, an efficient multidimensional array providing fast array-oriented arithmetic
'operations and flexible broadcasting capabilities.
'Mathematical functions for fast operations on entire arrays of data without having to write loops.
'Tools for reading/writing array data to disk and working with memory-mapped files.
'Linear algebra, random number generation, and Fourier transform capabilities.
"""
#%time for _ in range(10): my_arr2 = my_arr * 2


# to generater some random data
my_ndata=np.random.randn(2,3)
my_ndata*10

print("my ndarray data, and data shape and data type is ",my_ndata, my_ndata.shape,my_ndata.dtype)

data2 = [[1,2,3],[6,8,10]]
arr2= np.array(data2)

#np.zeros(),np.zeros(3,6)
# Create new arrays by allocating new memory, but do not populate with any values like ones and
print( np.empty((2, 3, 2) )  )

#If you have an array of strings representing numbers, you can use astype to convert them to numeric
numeric_strings = np.array(['1.25', '-9.6', '42'], dtype=np.string_)
numeric_strings.astype(float)

"""
Arithmetic with NumPy Arrays
call this vectorization,equal-size arrays applies the operation element-wise
"""

arr = np.array([[1., 2., 3.], [4., 5., 6.]])
print(arr*arr)
print(1/arr)
print(arr ** 0.5)

arr2 = np.array([[0., 4., 1.], [7., 2., 12.]])

if (arr2 > arr):
    print("arr2 is larger than arr")
else:
    print("arr2 is smaller")

