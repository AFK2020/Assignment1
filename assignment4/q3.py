from operator import add


n=int(input("Enter number of elements"))
k=int(input("Ebter how much shift you want"))

array=[]

for i in range(1,n+1):
    array.append(i)


print(array)

array2 = array[k+1:] + array[:k+1] 
print(array2)

array3=list(map(add,array,array2))  
print(array3)
array3.sort()
print(array3[0])
