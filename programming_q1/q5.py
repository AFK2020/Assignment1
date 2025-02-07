#Given an array of ints, return True if .. 1, 2, 3,.. appears in the array somewhere.

def array_check(array):
    for i in range(0,len(array)-2):
        if array[i]==1:
            if array[i+1]==2:
                if array[i+2]==3:
                    return True

    return False 


array=[1,2,3,2,5,1,3,5,12,45,1]

print(array_check(array))


