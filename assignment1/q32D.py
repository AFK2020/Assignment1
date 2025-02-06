#triangle pattern


row=int(input("Print number of rows"))
num=1

for i in range(1,row+1):
    print(" " * (row-i), end="")
    print("*" * (2*i -1))