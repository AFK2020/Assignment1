"""
n= int(input("Enter any number"))
count=0
lst=[]


for i in range(1,n+1):
    lst.append(i)

str_lst= list(map(str, lst))
print(str_lst)



for number in str_lst:
    if "1" in number:
        print("Number",number)
        count+=1

print(count)"""




n= int(input("Enter any number"))
count=0
lst=[]


for i in range(1,n+1):
    lst.append(i)

str_lst= list(map(str, lst))
print(str_lst)



for number in str_lst:
    if "1" in number:
        counter=number.count("1")       #using this so when it comes to 11 it will count 2 instead of one 
                                        #Using only "1" in number will count 11 as one time 1 instead of two
                                        #afifa! if you forget just remove this line and run till 13 
        count=count+counter

print(count)