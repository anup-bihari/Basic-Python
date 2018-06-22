from numpy import *
a=arange(1,10)
b=a.copy()
print("original array",a)
print("copied array",b)
b[0]=90
print("original array",a)
print("modified array",b)
