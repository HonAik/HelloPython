#1. 定义一个函数:根据传入的底和高计算三角形面积的函数(三角形面积=底*高/2)。

#user input
baseInput = int(input("Insert a number of base: "))
highInput = int(input("Insert a number of high:"))

#triangles area
def tri_area(base,high):
    return round(base*high*0.5,2)

#print result
print(tri_area(baseInput,highInput))

