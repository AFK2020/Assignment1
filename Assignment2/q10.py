
def factors(x):
    sum_perfect=0

    int_lst=[]

    for i in range(1,x):
        if x%i==0:
            int_lst.append(i)
    

    for j in int_lst:
        sum_perfect=sum_perfect+j
    
    return sum_perfect


if __name__=="__main__":

    for i in range(1,1000+1):
        result=factors(i)

        if i==result:
            print(i,"is a perfect number")
        else:
            print(i, "is Not perfect")