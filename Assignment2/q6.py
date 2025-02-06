#Binary to Decimal 

def B_to_D(binary):

    decimal=0
    i=0

    while binary>0:
        digit=binary%10     #take last digit
        decimal=decimal+((2**i)*digit)  
        i=i+1       #exponent value
        binary=binary//10
    
    return decimal



if __name__=='__main__':

    number=int(input("Enter Binary number"))
    print(B_to_D(number))

