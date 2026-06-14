"""
1. 生成1-20的平方列表。

2.从如下数字列表中提取所有偶数,并计算其平方,组成一个新的列表。

"""

# list1 = []

# for i in range(1,21):
#     num = i**2
#     list1.append(num)

# #a new way to write:
# # list1 = [i**2 for i in range(1,21)]

# newlist = []
# total = 0

# for i in list1:
#     if i%2 == 0:
#         newlist.append(i)
#         total += i
#     else:
#         continue

# print(f"the list of even numbers is{newlist} and the total number of them is {total}")

#the shortest way to write:
newlist = [i**2 for i in range(1,21) if i%2 == 0]

print(newlist)
print(sum(newlist))