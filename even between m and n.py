m,n=[int(x) for x in input("enter minimum and maximum").split(",")]
x=m
if x%2!=0:
      x=x+1

while x>=m and x<=n:
      print(x)
      x+=2
