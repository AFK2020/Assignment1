

def ion2e(str1):

    if str1[-3:]=='ion':
        return (str1[:-3]+'e')
    else:
        return str1
    


string1=input("Enter string")

print(ion2e(string1))
