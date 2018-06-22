#bubble sort implementation in python
from array import *
x=array("i",[])#empty array
print("enter how many element you want to enter",end=" ")
n=int(input())
for i in range(n):
           print("enter value of element",i+1,end=" ")
           x.append(int(input())) #add element to the existing array

print("original array",x)
flag=False
for i in range(n-1):
           for j in range(n-1-i):
                      if x[j]>x[j+1]:
                                 t=x[j]
                                 x[j]=x[j+1]
                                 x[j+1]=t
                                 flag=True
           if flag==False:
                      break
           else:
                      flag=False
print("sorted array",x)
