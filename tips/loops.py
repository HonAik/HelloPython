"""
if-loops
match
while-loops
for-loops
"""
#1.if-loops

# score = 920

# if score >900:
#     print("You are okay")
# else:
#     print("Nopeeeee")

#tutorial:
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

#tutorial：
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

day = input("Insert a day(1-7)")
match day:
    case "1":
        print("This is Monday")
    case "2":
        print("This is Tuesday")
    case "3":
        print("This is Wednesday")
    case "4": 
        print("This is Thursday")
    case "5": 
        print("This is Friday")
    case "6","7": # can use |
        print("This is weeknd")
    case _:
        print("This is an error")