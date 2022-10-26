#import numpy

thistuple=("A",12,'car','Banana',"C","B")

print("Print Tuple",thistuple)
print("access element by index",thistuple[1])
print("access element by negative index",thistuple[-1])
#notice that index 5 is not included
print("range from tuple",thistuple[2:5])
print("range from tuple, negative indexing",thistuple[-5:-1])
print(type(thistuple))

#check if item is in tuple
if 'Apple' in thistuple:
    print("yes item exists")
else:
    print("item doesnt exist")
    
#add into tuple
#to add/remove item we can change the tuple into list then add or remove using append and convert back to tuple
additem=("Y","Z",)
thistuple+=additem
print("Print Tuple",thistuple)
print(type(thistuple))

#delete the tuple
#del thistuple
print("Print Tuple",additem)

#unpack tuple items

(green, yellow, *red) = thistuple
(green, *yellow, red, blue) = thistuple
print(green)
print(yellow)
print(red)
print(blue)

#print items one by one in tuple
print("items in loop")
for i in range(len(thistuple)):
  print(thistuple[i])
  
#join tuples
thistuple2=("34","2",1)
newtuple=thistuple+thistuple2
print(newtuple)

#multiply tuple
thistuple3=thistuple2*2
print(thistuple3)

#tuple methods are index() and count()
print(thistuple2.index(1))

