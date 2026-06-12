#This file is witten for revision of basic python writting.
'''
Contents:
1.print()
    -print() 
    -boolean and int
2. Variable
    -type()
    -Identifier
    -isinstance()
    -',","""
    -\
    -concentrate
    -f-string
3. Summary print() and variables
'''

#1. print
# int,str,bool,none
# print(100) #int
# print(-1) #int
# print(3.2409284093) #float 
# print("Hello python") # str 
# print(True) #boolean, True False 
# print(None) #NoneType

# #boolean and int:
# #boolean is a type of int, True = 1, False = 0
# #example:
# print(True + 1) #2
# print(False - 1) #-1

# #2.Variable:
# # variable is a container stores a data value
# # Example:
# num = 5
# print(num) #5

# # a variable can store different type of value
# # can use type() for checking the type of variables.
# print(type(num)) #int 
# num = 10.02
# print(type(num)) #float
# num = True
# print(type(num)) #bool

# #tutorial:
# # A shop sold 10 soups a day, if tomorrow increase 10, how many soup will sell on tomorrow.
# base = 10
# incr = 10
# #can together : base,incr = 10,10
# print("The amount of soup are",base + incr) # use , for connect two different data types of variables

#Identifier标识符( & Naming rules of variable):
"""
1. variable only contains: numbers(0-9), alphabet(a-z,A-Z), underscore(_)
2. cannot start with number (0-9)
3. Variable names are case-sensitive (age, Age and AGE are three different variables)
4. cannot use Python keywords as a name(print,if,...)

Example: 
Correct: value1,myValue123,_,_myv1,fooo,VLQU1
Incorrect: 1my_, 234, .\[;m], my var 

"""
# #Tutorial:
# #a=10,b=20,now exchange their value
# a,b = 10,20
# a,b = b,a
# print(a,b)
# #instead of create a new variable for exchange, it can directly exchange on a same sentence

# #isinstance(variablename,datatype)
# #use for check the variables is the datatype that put in the ()
# num = 1000
# print(isinstance(num,int)) #return True
# print(isinstance(num,str)) #return False

# #about ',","""
# w1 = "Hello"
# w2 = 'Hello'
# w3 = """
# Hello:
#     I am Reynolds from Python diva world.
# """
# print(w1,w2,w3)
# print(type(w1),type(w2),type(w3))

# \
"""
\' = '
\" = "
\n = nextline
\t = tab

"""

#concentrate
# s1 = "Hi" "World" 
# print(s1)# HiWorld

# x=1
# y=2
# z="Hello"
# a="Python"

# print(x+y)  #3
# print(x,y)  #1 2
# #print(x+z)  #error(TypeError,int and str cannot add together)
# print(x,z)  #1 Hello
# print(z+a)  #HelloPython
# print(z,a)  #Hello Python

# print("Hello " + a + ", the number is", y)

#f-string
#use f-string when many variables need to put into a sentences
#f"sentences{variable}"

w2 = "Seli"
print(f"My name is {w2} ")



