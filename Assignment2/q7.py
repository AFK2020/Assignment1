#check if second is the multiple of first

def Multiple(a,b):
    
    if b%a==0:
        return True
    else:
        return False
    

if __name__=='__main__':

    int1=int(input("Enter first number"))
    int2=int(input("Enter second number"))

    print(Multiple(int1,int2))