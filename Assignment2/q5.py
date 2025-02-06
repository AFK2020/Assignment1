#write your own range function

def range_function(start,stop,step):
    lst_integers=[]

    while start<stop:
        lst_integers.append(start)
        start=start+step
    
    return(lst_integers)

if __name__ == "__main__":
    
    print(range_function(5,9,1))