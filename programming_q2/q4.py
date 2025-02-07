
list=[1444,6672,385,455,53,36,17,87,672,385,455]
lst2=[]

for i in range(len(list)):
    if list[i] in lst2:
        pass
    else:
        lst2.append(list[i])


print(lst2)

