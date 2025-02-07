#Write a function which should add the two vowels in the arrays and generate third array



string1=input("Enter string").lower()
string2=input("Enter second string").lower()

list_vowels=[
    "a",
    "e",
    "i",
    "o",
    "u",
]

arr1=[]
arr2=[]


for i in string1:
    if i in list_vowels:
        arr1.append(i)


for j in string2:
    if j in list_vowels:
        arr2.append(i)

arr1.extend(arr2)
print(*arr1)    # * removes commas from list

