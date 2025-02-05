"""21. Write a program that calculates the squares and cubes of the numbers from 0 to 10 and
uses tabs to print the following table of values:
number square cube
0 0 0
1 1 1
2 4 8
3 9 27
4 16 64
5 25 125"""

print("number \t square cube \n")
for i in range(0,11,1):
    print(i ,"\t", i*i ,"\t", i*i*i)
