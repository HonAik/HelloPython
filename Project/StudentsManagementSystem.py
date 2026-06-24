"""
采用面向对象的编程思想,完成教务管理系统的开发。教务管理系统可以管理在校学生的成绩信息,通过
控制台菜单与用户交互,具体的功能如下:

1. 添加学生成绩:根据输入的学生姓名、语文成绩、数学成绩、英语成绩,记录在系统中

2. 修改学生成绩:根据输入的学生姓名,修改对应的学生成绩

3. 删除学生成绩:根据输入的学生姓名,删除对应的学生成绩

4. 查询指定学生成绩:根据输入的学生姓名,查找对应的学生成绩,并输出

5. 展示全部学生成绩:展示出系统中所有学生的成绩

"""

#create a list store all student object
info = []

print("Welcome to use student management system")
print("""
    Here are the options:
    1.添加学生成绩
    2.修改学生成绩
    3.删除学生成绩
    4.查询指定学生成绩
    5.展示全部学生成绩
    6.退出系统
    """)

while True:

    class Student:

        def __init__(self,name,cs=None,ms=None,es=None):
            self.name = name
            self.cs = cs
            self.ms = ms
            self.es = es

        def __str__(self):
            return f"{self.name}\nChinese Score: {self.cs}\nMath Score: {self.ms}\nEnglish Score: {self.es}"
    
        def __eq__(self, other):
            return self.name == other.name
        
    
    userinput = int(input("Insert a number : "))

    match userinput:
    
        case 1:
    
            print("添加学生成绩")
            name = input("Insert a student's name: ")
            chineseScore = int(input("Insert the student's Chinese scores: "))
            mathScore = int(input("Insert the student's Math scores: "))
            englishScore = int(input("Insert the student's English scores: "))
            
            s = Student(name,chineseScore,mathScore,englishScore)

            exist = True

            for i in info:
                if i.name == s.name:
                    print("This students already exist")
                    exist = False
                    break

            if exist == True:
                info.append(s)

            for i in info:
                print(i)

            print("What is your next step (1-6),",end=" ")

        case 2:

            print("修改学生成绩")
            name = input("Insert a student's name you want to change: ")

            if name == s.name:
                cs1 = int(input("Insert the student's Chinese scores: "))
                ms1= int(input("Insert the student's Math scores: "))
                es1 = int(input("Insert the student's English scores: "))

                if chineseScore is not None:
                    chineseScore = cs1
                if mathScore is not None:
                    mathScore = ms1
                if englishScore is not None:
                    englishScore = es1
            else:
                print("cannot edit because this student is not on list.")

            for i in info:
                print(i)

            print("What is your next step (1-6),",end=" ")

        case 3:
            
            print("删除学生成绩")
            name = input("Insert a student's name you want to change: ")

            for i in info:
                if i.name == name:
                    info.remove(i)
                    break
                else:
                    print("cannot delete because this student is not on list.")

        case 4:
            print("查询指定学生成绩")
            name = input("Insert a student's name you want to change: ")

            for i in info:
                if i.name == name:
                    print(i)
                else:
                    print("cannot show because this student is not on list.")

        case 5:
            print("展示全部学生成绩")
            for i in info:
                print(i)
        case 6:
            print("Exit Successfully")
            break
        case _:
            print("Please insert a valid number between 1 to 5")
