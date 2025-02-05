""". Write a program to find the binary equivalent of the entered number., i.e. binary
equivalent of 170 is 10101010"""

number=int(input("enter number in decimal"))
binary_list=[]

while number>=1:
    digit=number%2
    print("digit",digit)
    binary_list.append(digit)
    number=number//2
    print(number)

binary_list.reverse()
print(binary_list)