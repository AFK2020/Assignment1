
string1=input("Enter string")

dict1={
    "a":0,
    "e":0,
    "i":0,
    "o":0,
    "u":0,
}

lst_vowels=[]

for i in string1:
    if i in dict1:
        dict1[i]=dict1[i]+1
        lst_vowels.append(i)


print(dict1)

lst_vowels.reverse()

print("Vowels in reverse order are:",lst_vowels)
