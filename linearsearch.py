#linear search
from array import *
x=array("i",[])#empty array

print("how many element you want to enter",end=" ")
n=int(input())
for i in range(n):
           print("enter elements",i+1,"=",end=" ")
           x.append(int(input()))
print("enter element to search",end=" ")
s=int(input())
flag=False
for i in range(len(x)):
           if s==x[i]:
                      print("found element at position =",i+1)
                      flag=True
if flag==False:
           print("Search element doesn't exist in the array")
