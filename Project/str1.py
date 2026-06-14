"""
1. 邮箱格式验证:用户输入一个邮箱,验证邮箱格式是否正确(包含一个@和至少一个.),如果输入正确,
输出“邮箱格式正确”,否则输出“邮箱格式错误”。

"""

email = input("Insert an email:")

if  email.count("@") == 1 and email.count(".") <= 1: #email.find("@") and email.find(".") and不必写 #and "." in email 也是可以

    print("Email format correct")
else:
    print("wrong email format")