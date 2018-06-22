str=[]
n=int(input("enter how many string you want to enter"))
for i in range(n):
      print("enter strings",end=" ")
      str.append(input())
print("enter a string you want to search")
searchstring=input()
flag=False
for i in str:
      print(i.title(),end=" ")
for i in range(len(str)):
      if searchstring==str[i]:
            print("found at ",i+1," postition")
            flag=True
            break
if flag==False:
      print("Not found")
      
