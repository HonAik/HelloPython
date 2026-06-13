#List introduction
"""
list
del
append()
insert()
extend()
remove()
pop()
sort()
reverse()

[::]

"""
#list can store many type of elements
# list1 = [12,"Hello",1.9,-1,False]
# It can have multiple elements, can modify and has order(start with 0)
# 
# Example:
# list1 = [1,2,3,4,5]
# list[0] = 1
# list[1] = 2
# list[4] = 5
# list[-1] = 5 

s = [12,23.344,"Hello",True,12]

# #list
# print(s[0]) #12
# print(s[1]) #23.344
# print(s[2]) # Hello
# print(s[3]) # Ture
# print(s[-1]) # True
# print(s[-2]) # Hello
# print(s[-3]) # 23.344
# print(s[-4]) #12

# #change
# s[2] = 12.34
# print(s[2]) #12.34

# #delete,del
# del s[0]
# print(s) #12 get delete

# #add
# #add at the end,append(element)
# s.append("python")
# print(s)

# #add inside, insert(space,element)
# s.insert(0,112233)
# print(s)

# #add another list together, extend()
# s2=[94,"but"]
# s.extend(s2)
# print(s)

#remove()，delete the first element that same in the remove(element)
# s.remove(12)
# print(s) # s[0] = 12 get deleted

#pop(),delete the element that same index number from pop(index number),if none number inside then delete the last one
# s.pop()
# print(s)

# s.pop(2)
# print(s)

#sort(),can order the list but must has the same data type in all element
q1 = [1,5,3,6,7,3]
q1.sort()
print(q1)

# #reverse(),reverse the list
# s.reverse()
# print(s)

# #loops for print each elements in sentences
# for i in s:
#     print(i)

# #list list using[start:end:step],end is not included
# q = [1,2,3,4,5,6,7,8,9]

# print(q[1:6:1])
# print(q[:6:2]) #从q[0]开始，中间空一个number