
set1={"apple","banana","cat","ball","bat"}
print(set1) 

#set doesnt allow duplicate values
set2={"apple","banana","cat",'cat',"ball","bat"}
print(set2) 
print(len(set2))

#diff datatypes
set3 = {"abc", 34, True, 40, "male"}
print(set3)

#type of set3
print(type(set3))

#use set constructor to create set
set4 = set(("apple", "banana", "cherry")) # note the double round-brackets
print(set4)

#access items in loop
for x in set4:
  print(x)
  
#print if item is present
print("banan" in set4)

#add itemsin set
set4.add("V")
print(set4)

#add 2sets

##set5=set3.add(set4) #this is not correct
print(set3.update(set4))

#add list and set
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

#remove items
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

thisset.discard("cherry")
print(thisset)

#pop
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)

#clear()
thisset.clear()
print(thisset)

#del
thisset = {"apple", "banana", "cherry"}
del thisset
#print(thisset)

#join 2 sets
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

#almost all join operations can be performed on sets