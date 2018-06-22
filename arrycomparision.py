#compare two array
from numpy import *
a=array([1,2,3,4,5])
b=array([0,2,3,22,4])
c=a==b
print("result of a==b",c)
c=a>b
print("result of a>b",c)
c=a<=b
print("result of a<=b",c)
