"""
合并两个列表中的元素,并对合并的结果进行去重处理(去除列表中的重复元素)。

# 定义列表

num_list1 = [19, 23, 54, 64, 875, 20, 109, 232, 123, 54]
num_list2 = [55, 80, 72, 35, 60, 123, 54, 29, 91]

解包
组包

"""
#Given list
num_list1 = [19, 23, 54, 64, 875, 20, 109, 232, 123, 54]
num_list2 = [55, 80, 72, 35, 60, 123, 54, 29, 91]

# combine together
num_list1.extend(num_list2)

#another easier way:
#new_list1 = [*num_list1,*num_list2] also can 
#new_list2 = num_list1 + num_list2 also can

#remove the duplication
#create a new list for after removing the duplication
num_list3 = []

#to put elements inside the new list
for i in num_list1:

    #decide elements are exists already in list
    if i in num_list3: #just write not in statement is okay already
        continue 

    elif i not in num_list3:
        num_list3.append(i)

print(num_list3)

