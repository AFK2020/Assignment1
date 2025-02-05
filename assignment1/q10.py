#Write a program that take year as an input from user. Determine whether year is leap year or not. 



def check_leap_year(year):
    if (year%100==0) and (year%400==0):
        return True
    elif(year%4==0) and (year%100!=0):
       return True
    else:
        return False


year=int(input("Enter Year to check"))
print("Is the year", year," leap year?", check_leap_year(year))