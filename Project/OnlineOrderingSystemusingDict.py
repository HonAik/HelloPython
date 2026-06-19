"""
开发一个购物车管理系统,实现商品信息的添加、修改、删除、查询功能。系统使用字典结构存储商品数据,
通过控制台菜单与用户交互。具体功能如下:

1. 添加购物车:用户根据提示录入商品名称、以及该商品的价格、数量,保存该商品信息到购物车。

2. 修改购物车:要求用户输入要修改的购物车商品名称,然后再提示输入该商品的价格、数量,输入完成后修改该商品信息。

3. 删除购物车:要求用户输入要删除的购物车名称,根据名称删除购物车中的商品。

4. 查询购物车:将购物车中的商品信息展示出来,格式为:“商品名称:xxx,商品价格:xxx,商品数量:xxx"。

5. 退出购物车
"""

print("Welcome use our online ordering list system")
text = """
#######list system###
#  1. add into list #
#   2. modify list  #
#   3. delete list  #
#   4. access list  #
#   5. exit list    #
######################
"""


#create a dict
d1 = {}

#
while True:
    
    user = input(text)
    print("Insert your number: ")

    match user:

     case "1":

        Iname = input("Insert item name: ")
        Iprice = float(input("Insert item price: "))
        Iamount = int(input("Insert item amount: "))

        if Iname not in d1:
            d1[Iname] = {"Price":Iprice,"Iamount":Iamount}
            print(d1)
        else:
            print("This items already exist")
        

     case "2":

        Ichange = input("Insert the items you want to change")

        if Ichange in d1:

            newIprice = input("Insert the items price")
            newIamount = input("Insert the items amount")

            d1[Ichange]= {"Price=" : newIprice,"Amount": newIamount}


        else:
            print("There is not an items call {Ichange} in your list")
        
     case "3":
        Iname = input("Insert the items you want to delete")

        if Iname in d1:
            del d1[Iname]
        else:
            print("Don't have this item")

        print(f"your list now:{d1}")
        
     case "4":
        Iname = input("Insert the items you want to access")

        if Iname in d1:
            print(d1[Iname])
        else:
            print("This items is not exist in list")
            
        """
        if you want access all:
        for items in d1:
            PandA = d1[items]
            print(f"name: {Items},Price ={PandA['Price']} ,Amount = {'PandA['IAmount']})
        """

     case "5":
        print("Exist successfully")
        break

     case _:
        print("Please type a number")
