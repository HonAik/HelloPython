import random

"""
猜数字游戏

1. 系统随机生成一个随机数

2. 用户根据提示猜数字,并将所猜的数字输入系统

3. 如果猜错,系统给出提示是猜大了,还是猜小了,然后继续输入猜的数字

4. 如果猜对,系统自动退出,游戏结束
"""


randomNumber = random.randint(1,100)

print("Guess the number between 1 to 100: ")

while True:

    num = int(input("Insert a number to guess: "))

    if num>randomNumber and num<=100 and num>=1:
        print("Your number is bigger than random number")
        continue

    elif num<randomNumber and num<=100 and num>=1:
        print("Your number is smaller than random number")
        continue

    elif num == randomNumber:
        print("Congratulations, you successfully guess a number")
        print(f"The number is {num}")
        print(f"Game is finished")
        break

    else:
        print("need to insert a number between 1 to 100")
        continue
