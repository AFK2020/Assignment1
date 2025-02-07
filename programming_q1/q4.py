
#Given a string and a non-negative int a, return a larger string that is n copies of
# the original string. eg string_times("Hi",3) = HiHiHi

def string_times(string,copies):
    print(string*copies)


string1=input("Enter string")
copy=int(input("Enter number of copies you want to print"))

string_times(string1,copy)