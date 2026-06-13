#Based on user input, find how many a and k from the input

countA = 0

countK = 0

words = input("Type somethings: ")

for i in words:

    if i =="a":
        countA +=1
    elif i == "k":
        countK +=1
    else:
        continue
    
print(f"A has {countA} and k has {countK}")