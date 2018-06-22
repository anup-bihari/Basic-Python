from numpy import *
a=matrix("1,2,3;4,5,6;7,8,9")
print(diagonal(a))
big=a.max()
small=a.min()
print(big,small,sep=",")
