#Python Operator
"""
1. Python Arithmetic Operators 加减乘除

x=1
y=2

print(x + y) #3 Addition
print(x - y) #-1 Subtraction
print(x * y) #2 Multiplication
print(x / y) #0.5 Division
print(x % y) #1 Modulus
print(x ** y) #1 Exponentiation 指数运算 1^2
print(x // y) #1 Floor division 向下取整 1/2=0.5=0 (不是1,因为是向下取整)

priority: **->*,/,//,%->+,-

2.Assignment Operators 
Operator	Example	        Same As
=	        x = 5	        x = 5	
+=	        x += 3	        x = x + 3	
-=	        x -= 3	        x = x - 3	
*=	        x *= 3	        x = x * 3	
/=	        x /= 3	        x = x / 3	
%=	        x %= 3	        x = x % 3	
//=	        x //= 3	        x = x // 3	
**=	        x **= 3	        x = x ** 3	
&=	        x &= 3	        x = x & 3
|=	        x |= 3	        x = x | 3	
^=	        x ^= 3	        x = x ^ 3	
>>=	        x >>= 3	        x = x >> 3	
<<=	        x <<= 3	        x = x << 3	
:=	        print(x := 3)	x = 3 
walrus operator             print(x)

Some explains:
1. &=

x=5
x &=3
change the number to binary and compare each 0 and 1,select 0

5 = 0101
3 = 0011
---------
& = 0001
#1

2. |=

x=5
x |=3
change the number to binary and compare each 0 and 1,select 1

5 = 0101
3 = 0011
---------
| = 0111
#7

3. ^=

x=5
x ^=3
change the number to binary and compare each 0 and 1, 
if same numbers with other put 0 otherwise 1

5 = 0101
3 = 0011
---------
^ = 0110
#6

4. >>=  

x=5
x >>=3

change the number(x=5) into binary and move the binary n steps to right depends on x>>=n, 
0 fill left shift

5 = 0101
move three steps to right
>>= 0000
#0

5. <<=
x=5
x <<=1

change the number(x=5) into binary and move the binary n steps to left depends on x<<=n, 
right put 0
5 = 0101
move one steps to left
<<= 1010
#10

6. :=,  Walrus Operator
assigns values to variables as part of a larger expression:

print(x:=5)

expression:
x=5
print(x)
#5

3. is,is not,in,not in, ==

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z) #true,point to the same object x
print(x == y) #true, the values inside the list are same 
print(x is y) #false, point to different object,x and y is different
print(x is not y) #true 
print("banana" in y) #true, banana is in the list
print("Banana" in y) #false, Banana and banana are not the same things
print("Mango" not in y) #true

"""