
def Alphabet_soup(string):
    longest=0
    punctuations_numbers = '''!()-[]{};:'"\,<>./?@#$%^&*_~0123456789'''


    for x in string:        #this for loop is to replace punctuations and numbers
        if x in punctuations_numbers:
            string = string.replace(x, "")

    sorted_list=list(string)

    for i in range(len(sorted_list)):
        for j in range(i+1,len(sorted_list)):
            if sorted_list[i]>sorted_list[j]:
                sorted_list[i], sorted_list[j] = sorted_list[j],sorted_list[i]
    

    sorted_string= "".join(sorted_list)
    return sorted_string





string = input("Enter string of your choice")

print(Alphabet_soup(string))