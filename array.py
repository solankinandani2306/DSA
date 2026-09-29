from numpy import *
a=array([1,2,3,4,5])
print(a)

a=array([1.1,2.2,3.3,4.4,5.5])
print(a)

a=array(['a','b','c','d','e'])
print(a)

a= array(['amar','bimal','cemma','dipak','rita'])
print(a)

a=linspace(0,10,5)
print(a)


a=logspace(1,4,5)
print(a)

import numpy as np
a=np.arange(1,10,3)
print(a)

a=np.zeros(5)
print(a)

a=np.ones(5)
print(a)

arr1=array([1,2,3,4,5])
print(arr1.ndim)

arr2=array([[1,2,3],[4,5,6]])
print(arr2.ndim)

arr1=array([1,2,3,4,5])
print(arr1.shape)

arr2=array([[1,2,3],[4,5,6]])
print(arr2.shape)

arr1=array([1,2,3,4,5])
print(arr1.size)

arr2=array([[1,2,3],[4,5,6]])
print(arr2.size)

arr1=array([1,2,3,4,5])
print(arr1.itemsize)

arr2=array([[1.1,2.1,3.5,4,5.0]])
print(arr2.itemsize)

arr1=array([1,2,3,4,5])
print(arr1.dtype)

arr2=array([[1.1,2.1,3.5,4,5.0]])
print(arr2.dtype)

arr2=array([[1,2,3],[4,5,6]])
print(arr2.nbytes)
