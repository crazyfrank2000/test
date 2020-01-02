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


""" 
tuple

"""
#tup = 1 , 2,44
nested_tup = (4, 5, 6), (7, 8)
# convert from list 
tup_convert=tuple([4, 0, 2])
tup_con_str = tuple('string')
print(tup_convert[0])
tup = tuple(['foo', [1, 2], True])
tup[1].append(888) 

tup_concat=(4, None, 'foo') + (6, 0) + ('bar',)*4


my_tuple=(12,999,0.888)
tuple1=("abc","def")
tuple2=my_tuple+tuple1

print(my_tuple)

"""
the swap can be done like this
"""
a, b = 1, 2
b, a = a, b

seq = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
for a, b, c in seq:
    print('a={0}, b={1}, c={2}'.format(a, b, c))
    
    
    
values = 1, 2, 3, 4, 5
a, b, *rest = values

# underscore (_) for unwanted variables
a, b, *_ = values


"""
List
"""

my_list = list(np.arange(100))
list1=[12,23,34]
list2=["asdfasdf","asdjfiasdf",list1,44]

list2.append(tuple2)
list2.insert(1,"insert @1")
#print(list2.pop(2))

list2.remove(44)
if 'asdjfiasdf' not in list2:
    print("asdjfiasdf is not in the list2")
else:
    print("inside")
    
    
    
gen = range(10)
print(list(gen))

#Concatenating and combining lists
x = [4, None, 'foo']
x.extend([7, 8, (2, 3)])

#Sorting
a = [7, 2, 5, 1, 3]
a.sort()
b = ['saw', 'small', 'He', 'foxes', 'six']
b.sort(key=len)

#Binary search and maintaining a sorted list

import bisect
c = [1, 2, 2, 2, 3, 4, 7]
print(bisect.bisect(c, 2))

#Slicing
seq = [7, 2, 3, 7, 5, 6, 0, 1]
print(seq[1:5])

seq[3:4] = [6, 3]
print(seq[:5])
print(seq[3:])

""
#to test the git function

#2020.1.1

"""
--------------------------end of today--------------------------------------------------
my_dict={'a':1,'b':2,'c':3}
print(my_dict.get('a'))
print(my_dict)



Now the numpy test code here 
The NumPy ndarray: A Multidimensional Array Object
key functions for ndarray
'ndarray, an efficient multidimensional array providing fast array-oriented arithmetic
'operations and flexible broadcasting capabilities.
'Mathematical functions for fast operations on entire arrays of data without having to write loops.
'Tools for reading/writing array data to disk and working with memory-mapped files.
'Linear algebra, random number generation, and Fourier transform capabilities.

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


Arithmetic with NumPy Arrays
call this vectorization,equal-size arrays applies the operation element-wise


arr = np.array([[1., 2., 3.], [4., 5., 6.]])
print(arr*arr)
print(1/arr)
print(arr ** 0.5)

arr2 = np.array([[0., 4., 1.], [7., 2., 12.]])

"""
