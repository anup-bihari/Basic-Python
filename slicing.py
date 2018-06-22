from array import *
x=array("i",[10,20,30,40,50,60,70])
y=x[1:4]
for i in y:
      print(i,end=" ")
print()
y=x[0:]
for i in y:
      print(i,end=" ")
print()
y=x[:4]
for i in y:
      print(i,end=" ")
print()
y=x[-4:]
for i in y:
      print(i,end=" ")
print()
y=x[-4:-1]
for i in y:
      print(i,end=" ")
print()
y=x[0:7:2]
for i in y:
      print(i,end=" ")
print()
