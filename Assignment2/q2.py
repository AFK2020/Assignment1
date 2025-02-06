# print prime numbers

import math

def prime_factors(n):
    while n%2==0:
        print("2")
        n=n/2

    for i in range(3,int(math.sqrt(n)+1),2):
        if n%i==0:
            print(i)
            n=n//i
    
    if n>2:
        print(n)
    

if __name__ == "__main__":

    prime_factors(11)

