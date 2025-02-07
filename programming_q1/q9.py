 

string='1234566'
count=0
int_string=list(string)
print(int_string)


for i in range(len(int_string)):
    if int(int_string[i])%6==0:
        print("i=",int_string[i])
        count=count+1
    for j in range(i+1, len(int_string)):
        digit=str(int_string[i])+str(int_string[j])
        if int(digit)%6==0:
            print("for loop",digit)
            count+=1


print(count)
