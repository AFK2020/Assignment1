
list_int=[1,2,3,4,6,5,4,9,8,4]
count=0

for i in range(len(list_int)):
    if list_int[i]==4:
        count+=1

print(count)