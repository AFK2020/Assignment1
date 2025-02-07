
letters={}
string1="ABCDBC"


for i in string1:
    if i in letters:
        letters[i]=letters[i]+1
    else:
        letters[i]=1
    

for key, value in letters.items():  #returns key value pairs in the form of list of tuples e.g [('A','1), ('B','2')] 
	print(f"{value}{key}",end="")