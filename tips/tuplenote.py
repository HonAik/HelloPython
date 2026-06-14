#tuple
# elements cannot modify #different with list
# has ordered
# has index
# can multiples

#how to write:
# tuple1 = (1,2.234,"Hello",True) or tuple1 = 1, 2.345 ,"Hello", True also can

# for empty:
# tuple2 = ()
# a = tuple()

#count(),same as str
#index(), same as str.find(),the one first element place only

# t1 = (12,24.432,"Hello")

# print(t1[2]) # Hello
# print(t1[:2]) # (12, 24.432)
# print(t1.index("Hello")) #2

# #if tuple only one elements:
# t2 = (100,)
# print(type(t2))

#unpacking:
t3 = 1,2.34,"Hello",True
# a,b,c,d = t3

# print(a,b,c,d) #1 2.34 Hello True

#(*) unpacking
x,*y,z = t3
print(x,y,z) #1 [2.34, 'Hello'] True
print(type(y))
#It will pack the less elements become together, and *y become a list 



