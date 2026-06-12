
"""
contents:
1.input
"""

#input:
# name = input("Insert a name:")
# print(f"My name is {name} ")

#tutorial:
# if u have 10000 in your bank, you want to take money, write code includes insert passwords, insert withdraw, show the less:
total = 10000

pw1 = 123456

pw2 = int(input("Insert passwords:"))

if pw1 == pw2 :
    
    m1 = input("Insert withdraw:")
    ml = total - int(m1)

    print(f"The amount of the less money is {ml}")

else:
    print("wrong passwords")
