

number= input("Enter number")
sum=0
lst=list(number)

for i in lst:
    i=int(i)
    sum=sum + (i*i*i)

if sum==int(number):
    print("Number is an armstrong")
else:
    print("Not armstrong")