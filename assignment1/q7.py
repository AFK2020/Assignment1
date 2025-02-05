#f a five-digit number is input through the keyboard, write a program to calculate the sum
#of its digits. (Hint: Use the modulus operator „%‟ to split the digits).


import math

def sum_cal(n):
    sum=0
    while n!=0:
        last_digit=n%10
        sum+=last_digit
        n=math.floor(n/10)
    
    return sum


Number=int(input("Enter five digit number"))
result= sum_cal(Number)
print("The sum of digits=", result)