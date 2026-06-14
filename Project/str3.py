"""
2. 将用户输入的10个字符串,反转后全部转换为大写,然后记录在列表中,最后将列表内容,遍历输出出来。
"""


words = input("Insert words")

new = words[::-1]

newU = new.upper()

newS = newU.split()

for i in newS:
    print(i)