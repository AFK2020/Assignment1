"""Write a program to generate all combinations of 1, 2 and 3 using for loop.
"""

for i in range (0,3,1):
    for j in range(0,3,1):
        for k in range(0,3,1):
            print(i+1,j+1,k+1)

