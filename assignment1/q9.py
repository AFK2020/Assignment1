"""A company insures its drivers in the following cases:
− If the driver is married.
− If the driver is unmarried, male & above 30 years of age.
− If the driver is unmarried, female & above 25 years of age.
In all other cases, the driver is not insured. If the marital status, sex and age of the driver
are the inputs, write a program to determine whether the driver is to be insured or not."""



Gender=input("Enter gender of employee \n F for Female \n M for male").upper()
marital_status=int(input("enter martital Status as \n 1 for married \n 2 for unmarried"))
age=int(input("Enter age of employee"))

if marital_status==1:
    print("Driver is insured")
elif Gender=='F' and age>25:
    print("Driver is insured")

elif Gender=='M' and age>30:
    print("Driver is insured")

else:
    print("Driver is not insured")
