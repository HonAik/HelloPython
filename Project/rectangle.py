#Question:
# Insert three lines of rectangle:
# 1. check these three lines can or cannot form a rectangle
# 2. if can, the rectangle is normal rectangle, Equilateral triangle,isosceles triangle.

#User input
line1 = int(input("Insert first line:"))
line2 = int(input("Insert second line:"))
line3 = int(input("Insert third line:"))

#check the rectangle:
# any two of the line should bigger than the third line
# rectangle1:5,6,3 Valid
# rectangle : 1,4,1 invalid

if line1 + line2 > line3 and line2 + line3 > line1 and line2 + line3 > line1:
    print("They can form a rectangle")
    if line1 == line2 ==line3:
        print("It is Equilateral triangle")
    elif line1 == line2 or line2 == line3 or line3 == line1:
        print("It is isosceles triangle")
    else:
        print("It is normal rectangle")
else:
    print("This is not a rectangle")