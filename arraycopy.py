from array import *
arr1=array("d",[1.5,2.5,-3.5,4])
arr2=array(arr1.typecode,(a*3 for a in arr1))
print("array 2 is have multiple of each elements of arr1")
for i in arr2:
      print(i)
