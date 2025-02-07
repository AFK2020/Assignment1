#Write a Python program to get the smallest number from a list.

list=[1444,6672,385,455,53,36,17,87]

smallest=list[0]

for i in range(len(list)):
    if list[i]<smallest:
        smallest=list[i]

print(smallest)
