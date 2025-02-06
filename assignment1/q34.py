row=int(input("Enter number of rows"))+2

for i in range(row//2):
    print("*" * i)


row_inverted=row//2

for j in range(row_inverted,0,-1):
    print("*" * j)