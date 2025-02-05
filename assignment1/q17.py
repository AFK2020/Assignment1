"""Given the length and breadth of a rectangle, write a program to find whether the area of
the rectangle is greater than its perimeter. For example, the area of the rectangle with
length = 5 and breadth = 4 is greater than its perimeter"""


length = float(input("Enter length of the rectangle: "))

breadth = float(input("Enter breadth of the rectangle: "))

area = length * breadth

perimeter = 2 * (length + breadth)

if area>perimeter:
    print("Area is greater")
else:
    print("Area is smaller")