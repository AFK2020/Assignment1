def isIn(string1,string2):
    if string1 in string2:
        return True
    elif string2 in string1:
        return True
    else:
        return False
    

if __name__ == "__main__":

    st1=input("Enter first string")
    st2=input("Enter second string")

    result=isIn(st1,st2)
    print(result)

