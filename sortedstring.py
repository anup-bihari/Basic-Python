str=[]
m=int(input("how many string"))
for i in range(m):
      print("enter string",end=" ")
      str.append(input())
print(str)
str1=sorted(str)
print("sorted list")
for i in str1:
      print(i)
