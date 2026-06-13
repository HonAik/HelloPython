"""
需求:根据输入的用户名密码执行登录操作,具体要求如下:

1. 正确的用户名和密码为admin/666888、zhangsan/123456、taoge/888666

2. 输入用户名和密码进行登录,直到登录成功,程序结束运行;如果登录失败,则继续输入用户名和密码进行登录

3. 输入的用户名和密码不能为空!

4. 登录成功:输出“登录成功,进入B站首页~”

5. 登录失败:输出“用户名或密码错误,请重新输入!”
"""
a = True

while a:

    un1 = input("Insert your username:")
    pw1 = input("Insert your passwords:")

    match un1:
        case "admin":
            if pw1 == "666888":
                print("Successfully access")
                a = False

            elif pw1 == None:
                print("passwords cannot be empty, please insert again")
            else:
                print("Username or passsword is wrong, please insert again")
    
        case "zhangsan":
            if pw1 == "123456":
                print("Successfully access")
                a = False
            elif pw1 == None:
                print("passwords cannot be empty, please insert again")
            else:
                print("Username or passsword is wrong, please insert again")

        case "taoge":
            if pw1 == "888666":
                print("Successfully access")
                a = False
            elif pw1 == None:
                print("passwords cannot be empty, please insert again")
            else:
                print("Username or passsword is wrong, please insert again")

        case _:
            print("Username or passsword is wrong or empty, please insert again")

#This can but only 90/100 because while+if more readable,
"""
while True:

    ........ #user input

    if..... # for empty
    continue # to go back

    if...... # for admin 
     ......
     break #instead of truefalse
    elif.....# for zhangsan
    elif.....# for taoge
    else.....# for wrong

"""