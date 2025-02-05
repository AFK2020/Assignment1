#. Temperature of a city in Fahrenheit degrees is input through the keyboard. Write a
#program to convert this temperature into Centigrade degrees.


Faren=float(input("Enter temp in Fahrenheit"))
Celcius=round((Faren-32)*(5/9),2)

print("Temp in Celcius=", Celcius,"C")

