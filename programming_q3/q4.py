

#Write a Python program to calculate the sum of three given numbers, if the values are
#equal then return thrice of their sum

number=int(input("Enter number"))
number2=int(input("Enter number"))
number3=int(input("Enter number"))
sum=0


if number==number2 and number2==number3:
    sum=number+number2+number3
    print(3*sum)


else:
    sum=number+number2+number3
    print(sum)