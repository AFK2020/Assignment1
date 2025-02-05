
"""If the three sides of a triangle are entered through the keyboard, write a program to check
whether the triangle is isosceles, equilateral, scalene or right-angled triangle"""


a = float(input("Enter the length of the first side of a triangle: "))

b = float(input("Enter the length of the second side of a triangle: "))

c = float(input("Enter the length of the third side of a triangle: "))

if (a == b and b == c and c == a):
    print("Equilateral Triangle.")

elif (a == b or b == c or c == a):
    print("Isosceles Triangle.")

elif (a != b and b != c and c != a):
    print("Scalene Triangle.")

elif ((a**2)+(b**2)==(c**2) or (c**2)+(b**2)==(a**2)) or (a**2)+(c**2)==(b**2):
    print("Right angle Triangle")