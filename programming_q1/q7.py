#Given 3 int values, a b c, return their sum. However, if one of the values is the
# same as another of the values, it does not count towards the sum.



def lone_sum(a,b,c):
    sum=0
    lst_sum=[]
    if a==b and a==c:
        sum=0
    elif a==b:
        sum=c
    elif a==c:
        sum=b
    elif b==c:
        sum=a
    
    else:
        sum=a+b+c
    
    return sum


a=int(input("Enter first number"))
b=int(input("Enter first number"))
c=int(input("Enter first number"))

print(lone_sum(a,b,c))
