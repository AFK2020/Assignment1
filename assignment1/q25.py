"""Write a program to find the range of a set of numbers. Range is the difference between
the smallest and biggest number in the list. You are not allowed to use built-in range()
function"""

"""
range=[]

num= 0

while num>=0:
    num=int(input("Enter number greater than 0. Enter -1 to exit"))
    range.append(num)

minimun=min(range)
maximum=max(range)

print("Range is", maximum-minimun)
"""

interations=int(input("How many numbers do you want to enter"))
number=int(input("Enter first number"))
min=max=number
count=0 

while interations-1>count:
    number=int(input("Enter number"))
    count=count+1
    if(number>max):
        max=number
    elif(number<min):
        min=number
    else:
        pass

range=max-min
print("Range=",range)