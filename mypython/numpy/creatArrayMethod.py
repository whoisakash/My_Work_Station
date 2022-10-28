import numpy as np

#1 Creat array: Conversion from other python structure (e.g. List, Tuple)
listarray = np.array([[1,2,5], [4,6,8], [8,9,7]])
# change value
# listarray[1,1]=15

# find Size, Shape, dtype
# print(listarray.shape)
# print(listarray.size)
# print(listarray.dtype)

# dtype = object
# dt_object= np.array({24,34,34})
# print(dt_object.dtype)
'''most of case use int and float use more implace of object'''


#2 Creat array: Intrinsic numpu array creation object(e.g. arange, ones, zeros)
#2.1 zeros
# zeros = np.zeros((2,5))
# print(zeros.dtype)

#2.2 arange
rng = np.arange(15)
# print(rng)

# 2.3 linspace(1st element,Last element,total element) : gives equaly devied space point
lspace = np.linspace(1,50,10)
# print(lspace)

# 2.4 empty: creat array of reandom value
emp = np.empty((5,2), np.int64)
# print(emp)

# 2.5 empty_like: copy array size and fill reandom value
emp_like = np.empty_like(lspace)
print(emp_like)

# find element in array, give position as (row, column) formate
ar = np.array([[1,2,3],[4,5,6],[7,1,0]])
# print(ar)
# find_ele = np.where(ar>5)
# print(find_ele)

# count non zeero element
# non_zero = np.count_nonzero(ar)
# non_zero = np.nonzero(ar)
# print(non_zero)

# ar[0,1]=0
# print(ar)
# non_zero = np.nonzero(ar)
# print(non_zero)

# check how space saver is numpy then list
import sys
# py_ar = [[1,2,3],[4,5,6],[7,1,0]]
# print(len(py_ar),py_ar)
# npy_ar = np.array(py_ar)
# print(npy_ar.itemsize,npy_ar)
#
# py_size= sys.getsizeof(1)*len(py_ar)
# print("py_size",py_size)
# npy_size = npy_ar.itemsize * npy_ar.size
# print("npy_size",npy_size)
