"""
根据提供的班级学生的选课情况,完成如下需求:

1. 找出同时选修了法语和艺术的学生

2. 找出同时选修了所有四门课程的学生

3. 找出选修了足球,但是没有选修篮球的学生

4. 统计每一个学生选修的课程数量

"""

football = {"Reynolds","Dennis","Ray","Dorcas","Nikk","Jelena","Cindy"}

french = {"Ray","Jelena","Cindy","Danny","Thomas","Adeline","Joey","Reynolds"}

basketball ={"Brian","Nelson","Vennis","Dorcas","Hayden","Joey","Reynolds"}

art = {"Brian","Thomas","Reynolds","Ray","Joey","Adeline","Cindy"}

#1
print(f"{french.intersection(art)}")
#or using &
print(french&art)

#2
print(f"{football.intersection(french.intersection(basketball.intersection(art)))}")

#3
print(football.difference(basketball))
#or using -
print(football-basketball)

#or方式三:集合推导式 --- >快速构建集合,语法:{要往集合中添加的数据 for s in set1 if 条件} 
print({i for i in football if i not in basketball})

#4
#解题思路：先有一个set关于全部学生的名字，然后制作一个list for store 全部set的资料 然后在for i in set then print

all_set = basketball | art | football | french
#union() 也可以

all_list = [*basketball,*art,*football,*french] #unpacking from list

for i in all_set:
    print(f"{i} attempts {all_list.count(i)}")
