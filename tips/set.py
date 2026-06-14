#set
"""
add()
remove()
pop()
clear()
difference()
union()
intersection()
"""
# cannot duplicate
# unorder
# no index
# can modify

#set ={"a","b"}

#empty
#s2 = set()

s1 = {12,34,"sdf",3455,True,12}

print(s1) #not always same because no index
print(type(s1)) #set

#add(),add elements inside
s1.add(1245)
print(s1)

#remove(),remove elements
s1.remove(34)
print(s1)

#pop(),randomly delete elements
s1.pop()
print(s1)

#difference(),only take s2's elements that has not same in s1
s2={124,523,True}
print(s1.difference(s2))

#union(),combine sets together
print(s1.union(s2))

#intersection() ,find the same elements with another set
print(s1.intersection(s2))

#clear(), clear all the elements from the sets
print(s1.clear())







