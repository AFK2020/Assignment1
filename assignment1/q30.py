"""Write a program that takes the side of a square from user and then prints that square out
of asterisks. Your program should work for squares of all side sizes between 1 and 20.
For example, if your program reads a size of 4, it should print
****
****
****
****
"""

side=int(input("Enter size of square"))

for i in range(0,side):
    print("*",end="")
    for j in range(0,side-1):
        print("*",end="")
    print()     #new line