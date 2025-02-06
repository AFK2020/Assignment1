#octal equivalent


number=int(input("Enter number"))
octal_list=[]

while number>=1:
    digit=number%8
    octal_list.append(digit)
    number=number//8

octal_list.reverse()
print(*octal_list) #print without commas