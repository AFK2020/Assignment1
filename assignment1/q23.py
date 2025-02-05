#Write a program to enter the numbers till the user wants and at the end it should display
# the count of positive, negative and zeros entered.

num =0
count_negative=0
count_zero=0
count_positive=0


while num!=-999:
    num=int(input("Enter number and enter -999 to exit"))
    if(num<0):
        count_negative+=1
    elif(num>0):
        count_positive+=1
    elif(num==0):
        count_zero+=1
    else:
        print("Invalid Number")

print("Positive Numbers", count_positive)
print("Negative Numbers", count_negative-1)
print("Zero count", count_zero)