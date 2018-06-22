from numpy import *
a=arange(1,10)
b=a.view()
print("original array",a)
print("new array",b)
b[0]=99
print("modified a array",a)
print("modified in b array",b)
