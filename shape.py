from numpy import *
arr=array([[1,2,3],[4,5,6]])
print(arr.shape)
arr.shape=(3,2)
print(arr.shape)
for i in arr:
      print(i)
print(arr.itemsize)
print(arr.dtype)
arr=arr.reshape(3,2)
print(arr)
arr=arr.flatten()
print(arr)
