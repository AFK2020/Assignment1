
try:
    num=int(input("ENter a number"))
    print(1/num)

except ZeroDivisionError:
    print("IDIOT! You can't divide by zero")

except ValueError:
    print("Enter only numbers please")

except Exception:
    print("Something went wrong")

finally:    #this always execute
    print("End of code")