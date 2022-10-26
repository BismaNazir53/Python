#insert
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

#append
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#add 2 lists
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#add 2 different iterables
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

#remove
thisset = ["apple", "banana", "cherry"]
thisset.remove("banana")
print(thisset)

#pop
thisset.pop()
print(thisset)

#delete
thislist = ["apple", "banana", "cherry"]
del thislist[0:2]
print(thislist)

#delete complete list
thislist = ["apple", "banana", "cherry"]
del thislist

#clear list
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#items 1 by 1
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
#OR 
for i in range(len(thislist)):
  print(thislist[i])

#while loop 
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
  
#create new list base on some other list
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)

#create new list
newlist = [x for x in range(10) if x < 5]
print(newlist)

#create upper letters
newlist = [x.upper() for x in fruits]
print(newlist)

#sort
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
#OR revrse order sorting
thislist.sort(reverse = True)
print(thislist)

#copy list
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
#OR
list1=thislist
print(list1)
#OR
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

#add join append lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

#OR
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print(list1)

#OR
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)


Name='Bisma'
print(Name.find("is"))


#concatenate lists
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list3=list1+list2
print("list3 is ",list3)

del list3[2:5]
print("list3 deleted", list3)
