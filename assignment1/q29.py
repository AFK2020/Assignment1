row=int(input("Print number of rows"))
num=1

for i in range(1,row+1):
    print(" " * (row-i), end="")
    for j in range(i):
        print(num,end=" ")
        num=num+1
    print()
