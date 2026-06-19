#dict,
"""
-
"""

#define dixt:
# dict = { key : value}
# a key corrresponds to a value, it cannot be duplicated but can modify, if key has duplicated, then the back one will cover the front one 
# value can be any type of data such as int,bool,str,float,set,..... 
# key cannot be the type that changeable such as: set,list,dict...
#empty dict:
# d1 = {}
# d2 = dict() , same as set()

#use key to access value
# value = d1[key]

d1 = { 1:123, 2.3:"Je;ade", (1,2):"sdf",123:123}

#add:
#if you want to add a new value, u must add a new key also
d1["Hello"] = "Python" 
# d1 has no a key calls "Hello" so it will be added into d1 and "Python" as its value.

#modify:
# if you want modify some value, use their key and assign the new value

print(d1[1]) #original

d1[1]=234 #change

print(d1[1]) 

#delete:
# if you want to delete a value, there are 2 ways:

#1. use pop():
d1.pop(2.3)
print(d1) #{2.3:"Je;ade"} get deleted

#2. del
d1[9] = 10
print(d1)

del d1[9]
print(d1)

#access:
#There are four way:
# 1. use their key to print:
print(d1[1]) 

# 2. use get()
print(d1.get(1))

# 3. use keys() for get all the key 
print(d1.keys())

# 4. use values() for get all the value
print(d1.values())

# 5. use items() to print the key pairs with their value
print(d1.items())

#if you want to print the value and key using for
for key in d1:
    print(f"{key} : {d1[key]}")

