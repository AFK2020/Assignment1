#find mean median mode

import random
from collections import Counter


numbers=10
lst=[]
sum=0

for i in range(numbers):
    random_number = random.randint(0,10)
    lst.append(random_number)

for j in lst:
    sum=sum+j

mean=sum/numbers
if numbers%2!=0: #odd number of values
    Median = lst[int((numbers + 1)/2)]
elif numbers%2==0:      #for even number of values
    Median=(lst[int(numbers/2)])+ lst[int((numbers/2) + 1)]/2 

print(round(mean,3),round(Median,3))


length_lst=len(lst)

data=Counter(lst)   #it returns a dictionary like object
frequency=dict(data) #convert it into list

mode = [k for k, v in frequency.items() if v == max(list(data.values()))] #list comprehension
                                                            #for key element in dictionary and we are
                                                            #iterating through dictionary by using keys
                                                            #and v is the values of those keys
                                                            #item() coverts dictionary key value into tuples

if len(mode) == numbers: 
    frequency = "No mode found"
else: 
    frequency = "Mode is / are: " + ', '.join(map(str, mode)) #make each item in mode a string
                                        #join: joins the items is mode and seperate by comma


print(frequency)

