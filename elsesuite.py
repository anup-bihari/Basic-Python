#search for an element in the list
group1=[1,2,3,4,5]
search=int(input("enter an element to search:\n"))
for element in group1:
      if search==element:
            print("element found in group1")
            break
else:
      print("element not found in group 1")
