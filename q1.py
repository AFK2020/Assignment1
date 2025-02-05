#Write a program that asks the user to enter two numbers, obtains them from the user and
#prints their sum, product, difference, quotient and remainder.


num1=int(input("Write first number"))
num2=int(input("Write second number"))

print("Sum =",num1+num2)

print("Product =",num1*num2)

print("Difference =",num1-num2)

print("Qoutient =",round((num1/num2),2))

print("Remainder =",num1%num2)