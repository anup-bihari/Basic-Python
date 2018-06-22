#transpose of matrix
from numpy import *
r,c=[int(a) for a in input("enter rows and column").split()]
print("enter element in the matrix")
str=input("enter elements")
#converting string into matrix
x=reshape(matrix(str),(r,c))
y=x.transpose()
print("original matrix\n")
print(x)
print("transpose matrix\n")
print(y)
