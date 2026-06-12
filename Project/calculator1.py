#use match...case create a calculator

num1 = float(input("Insert a number: "))
num2 = float(input("Insert another number: "))
oper = input("Insert a operator(+,-,*,/): ")

match oper:
    case "+":
        print(f"{num1} + {num2} = {num1 + num2}")
    case "-":
        print(f"{num1} - {num2} = {num1 - num2}")
    case"*":
        print(f"{num1} * {num2} = {num1 * num2}")
    case"/":
        if num2 >0:
            print(f"{num1} / {num2} = {num1 / num2}")
        else:
            print(f"numbers cannot divided by {num2}")
    case _:
        print("This is an error")