import sys
from numpy import *
r1,c1=[int(a) for a in input("first matrix rows,cols:").split()]
r2,c2=[int(a) for a in input("first matrix rows,cols:").split()]
if c1!=r2:
      print("Aap jo bhi multiplication kar rahe hai wo nahi ho sakta")
      sys.exit()
str1=input("enter first matix element")
x=reshape(matrix(str1),(r1,c1))
str2=input("enter second matrix element")
y=reshape(matrix(str2),(r2,c2))
print("the product of matrix is\n")
z=x*y
print(z)
