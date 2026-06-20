#calculate n factorials

x = int(input("Insert a number: "))

def fact(a):
    if a == 1:
        return 1
    else:
        return a * fact(a-1)

print(fact(x))

