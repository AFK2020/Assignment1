
row=int(input("Enter number of rows"))

for i in range(row+1):
    print("*" * i)


print()
print()


row_inverted=int(input("Enter number of rows"))

for j in range(row_inverted,0,-1):
    print("*" * j)