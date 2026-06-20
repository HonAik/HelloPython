#function:

# how to write:
# def funcitonname(parameter):
#    .......
#    return
#
#functionname()

# def line():
#     print("Hello")

# line()

# tutorial1:
# calculate circle area:
# def circle_area(r):
    
#     c_area = 3.14 * r * r
#     return c_area

# area = circle_area(10)
# print(area)

#if parameter has more than 1, use"," to seperate
# example:
# def example(a,b)

#tutorial2: print circle area and length:
# def circle_area_len(r):
#     return 3.14*r**2, round(2*3.14*r,1)#round() use for decimals
# print(circle_area_len(10)) # the answer will be into set!

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# num = 100

# def ab(b):
#     a = 2
#     num = 10*a
#     return num

# print(num)
# print(ab(num))
# print(a) # cannot print
# print(b) #cannot print
# a and b cannot print bacause it only can be accessed in the function ab() area

# the num is used but it is not the outside num which is 100
# if you want used outside num, use "global"

# num = 100

# print(num)

# def ab():
#     global num
#     num = 10
#     print(num)

# ab()
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

#parameter

# def info(name,age,gender,city):
#     print(f"name={name},age={age},gender={gender},city={city}")

# info("Reynolds",21,"male","Selongor") # directly 

# info(name="Reynolds",age=21,gender="male",city="Selongor") #can wirte parameter inside

# info("Reynolds",21,gender="male",city="Selongor") #write some but some didnot

# #info(name="Reynolds",age=21,"male","Selongor"),error,must didnot first and then some last

# def info1(name,age,gender,city = "KL"):#defalut parameter only can be last, cannot infornt like(name="A",age,...) cannot
#     print(f"name={name},age={age},gender={gender},city={city}")

# info1("Jack",12,"male")
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#*args
#if you have many many many data need to put into parameter, try use *args
# u can write *a,*abcde,*hde whatever u want

#calculation highest,smallest and avr
# def cal(*args):# *args is a tuple and u unpacking it
#     high = max(args)
#     mins = min(args)
#     avg = round(sum(args)/len(args),1)
#     return high,mins,avg

# h,m,a =cal(23,454,634,67,34,64,6,45,45)
# print(h,m,a)

#but if you have some parameter which is a=12,b=44.... 
# use **kwargs,dict
#also **a,**b also can 

# def cal(*args,**kwargs): # *first,** last
#     high = max(args)
#     mins = min(args)
#     avg = sum(args)/len(args)

#     if kwargs.get('round'):
#         avg = round(avg,kwargs.get('round'))

#     return high,mins,avg


# data=cal(12,13,234,12,12,213,round = 2,num = 1)
# print(data)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#function also can be a parameter
# def add(x,y):
#     return (x+y)

# def info(x,y,oper):
#     return oper(x,y)

# data = info(12,14,add)
# print(data)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#lambda is used if u dont want to declare a method
# a = lambda x,y : x+y
# print(a(10,20))

# b= lambda : print("Hello")
# b()

#tutorial:
# use list to sort the words with their length,small to big
list =["a","abcde","are","C++","C","aaaaaa","Python"]

list.sort(key= lambda i : len(i)) #key = len also can 

print(list)

list.sort(key= lambda i : len(i),reverse=True)

print(list)
