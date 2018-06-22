x=int(input("enter a number greater than 0:"))
try:
      assert x>0
      print("u enterd:",x)
except AssertionError:
      print("wrong input entered")
