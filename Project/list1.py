"""
1. 将用户输入的10个数字,存储到一个列表中,并将列表中的数字进行排序,输出其中的最小值、最大值
和 平均值。

-sum() and len()

"""
#create a list
user = []

#input:
for i in range(10):
    num = int(input("Insert 10 numbers: "))
    user.append(num)

#sort
user.sort()
print(user)

#find the smallest
print(user[0])

#find the biggest
print(user[-1])

#average
# total = 0
# count = 0

# for i in user:
#     total += i
#     count += 1

#print(f"The average is {total/count}")

#but we can use sum() and len()

print(f"The average is {sum(user)/len(user)}")


