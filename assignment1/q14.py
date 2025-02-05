"""Write a program that inputs three different integers from the keyboard (i.e num1, num2,
num3), then prints the sum, the average, the product, the smallest and the largest of these
numbers. The screen dialogue should appear as follows:
Enter three different integers: 13 27 14
Sum is 54
Average is 18
Product is 4914
Smallest is 13
Largest is 27"""

print("Enter three numbers")

integer1=int(input("Enter first number : "))
integer2=int(input("Enter second number : "))
integer3=int(input("Enter third number : "))

print("Sum", integer1+integer2+integer3)
print("Average", round((integer1+integer2+integer3)/3,2))
print("Product", integer1*integer2*integer3)
print("Smallest", min(integer1,integer2,integer3))
print("Largest", max(integer1,integer2,integer3))



