#Write a program that reads in two integers and determines and prints whether the first is a 
# multiple of the second. [Hint: Use the remainder operator.


integer1=int(input("Enter first number : "))
integer2=int(input("Enter second number : "))

if (integer1%integer2==0):
    print(integer1,"is a multiple of", integer2)
else:
    print("It is not a multiple")