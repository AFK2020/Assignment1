#Write a Python program to get the difference between a given number and 17, if the
# number is greater than 17 return double the absolute difference.

number=int(input("Enter number"))

if number>17:
    print(2*abs((17-number)))

else:
    print(17-number)