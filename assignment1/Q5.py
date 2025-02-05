#The length & breadth of a rectangle are input through the keyboard. Write a program to
#calculate the area & perimeter of the rectangle.



length = float(input("Enter length of the rectangle: "))

breadth = float(input("Enter breadth of the rectangle: "))

area = length * breadth

perimeter = 2 * (length * breadth)

print("Area of rectangle = ", area)
print("Perimeter of rectangle = ", perimeter)