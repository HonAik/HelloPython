"""
if-loops
match
while-loops
for-loops
range()
nested-loops
Question

"""

#1.if-loops

# score = 920

# if score >900:
#     print("You are okay")
# else:
#     print("Nopeeeee")

#tutorial1:
#if you want to access an account, you need to type your passwords and account number if both correct 
# then u can successfully access the system

# acc = "Reynolds" 
# password = 12345

# acc_ip = input("Insert account number: ")
# pw1 = int(input("Insert passwords: "))

# if acc_ip == acc and pw1 == password:
#     print("Login successfully")
# else:
#     print("Login failed")

#tutorial2：
"""

1. 需求1:根据用户输入的数字,判断该数字是奇数还是偶数。

2. 需求2:根据用户输入的年龄,判断该用户是否已经成年(>=18,成年;否则,未成年)。

3. 需求3:根据用户输入的数字,判断该数字是正数还是负数(不考虑0)。

4.需求4:根据用户输入的考试分数,判断该分数是否及格了(大子等于60就是及格了)。

"""

# num1 = int(input("Insert a number : "))
# if num1 %2 == 0:
#     print(f"{num1} is an even number")
# else:
#     print(f"{num1} is an odd number")

# age = int(input("Insert age : "))
# if age >= 18:
#     print("You are above 18")
# else:
#     print("You are below 18")

# num2 = int(input("Insert a nember : "))
# if num2 >0:
#     print("This is a positive number")
# elif num2 == 0:
#     print("Cannot put zero")
# else:
#     print("This is a negative number")

# score = int(input("Insert score: "))
# if score >= 60:
#     print("You are passed")
# else:
#     print("You are failed")

#2. match
# same as switch from java:

# day = input("Insert a day(1-7)")
# match day:
#     case "1":
#         print("This is Monday")
#     case "2":
#         print("This is Tuesday")
#     case "3":
#         print("This is Wednesday")
#     case "4": 
#         print("This is Thursday")
#     case "5": 
#         print("This is Friday")
#     case "6","7": # can use |
#         print("This is weeknd")
#     case _: # default
#         print("This is an error")

#while
#same as java:
#need to know the condition to stop and start (no need to know how many times to loop - for-loops is for that)
"""
while True:
    .......

while True:
    ........
else:
    False

"""

#tutorial3:
#print 10 times (I love Python) using while:
# i=0
# while i<10:
#     print("I love Python")
#     i+=1
# else:
#     pass

#tutorial4:
#calculate the addition of even numbers between 1-100:

# num = 1
# count =0

# while num <= 100:

#     if num%2 == 0:

#         count += num

#     num += 1

# print(f"The total is {count}")

#for
"""
for...in...:
    ........
else:
    ........
"""

# words = "Hello Python"
# count = 0
# for i in words:
#     print(f"Elements:{i}")
#     count +=1
# else:
#     print("finished")

# print(count)

#tutorial5:
#calculcate the addition of odd numbers between 1-100:

"""
range():use in int
range(end):start from 0 to end(not include end)
range(start,end):start to end(not include end)
range(start,end,step):start to end(not include end), step between each words

"""

# count = 0

# for i in range(101): # also can write as: for i in range(1,101,2):count +=1
#     if i %2 !=0:
#         count +=i

# print(f"The count is {count}")

#tutorial6:
#calculate the addition of numbers that multiples of three between 100-500
# count = 0

# for i in range(100,501):
#     if i %3 == 0:
#         count += i

# print(count)

#nested-loops
#tutorial7 !!!very important
#print a rectangle that has m(*) length and n(*)width

# m = int(input("Insert the length: ")) 
# n = int(input("Insert the width: ")) 

# for i in range(n): #control line

#     for i in range(m):  #control elements
#         print("*",end =" ")
    
#     print()

#tutorial8:
#create a multiples table (1-12):

# for j in range(1,13):
#     for i in range(1,13):
#         print(f"{i} x {j} = {j*i}")
#     print()

#if I want the line same as the number for example:
#  1 has 9 (start with 1x1)
#  2 has 8 (start with 2x2)
#  3 has 7 (start with 3x3)
#  ..... 
#  9 has 1 (only 9x9) 
#  end
# for j in range(1,10):
#     for i in range(j,10):
#         print(f"{j} x {i} = {j*i}")
#     print()

#now I want range them more readable!!!

# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f"{i} x {j} = {i*j}", end="  ")
#     print()

#tutorial9:
# Based on users input,print the number triangle like above 

# num1 = int(input("Insert a number: "))
# num2 = int(input("Insert a number: "))

# for i in range(num1,num2+1):
#     for j in range(num1,i+1):
#         print(j,end=" ")
#     print()

#tutorial10
#Based on user input, create a right triangle with the same length that user input

length = int(input("Insert a number: "))

for i in range(length+1):
    for j in range(1,i+1):
        print("*" , end=" ")
    print() 




