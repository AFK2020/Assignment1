

string = input("Enter string of your choice")
longest=0


punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
 

for x in string:        #this for loop is to replace punctuations
    if x in punctuations:
        string = string.replace(x, "")


list_string=string.split()

for i in list_string:
    if len(i)>longest:
        word=i
        longest=len(i)

print("The longest word is", word, "with the length=",longest)
