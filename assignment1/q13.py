"""Write a program that asks the user to enter two integers, obtains the numbers from the
user, then prints the larger number followed by the words “is larger.” If the numbers are
equal, print the message “These numbers are equal.” Use only the single-selection form
of the if statement you learned in this chapter."""


integer1=int(input("Enter first number : "))
integer2=int(input("Enter second number : "))

if(integer1==integer2):
    print("They are equal")


if(integer1>integer2):
    print(integer1,"is larger than", integer2)


if(integer2>integer1):
    print(integer2,"is larger than", integer1)
