"""(Body Mass Index Calculator) We introduced the body mass index (BMI) calculator in
The formulas for calculating BMI are
BMI = (weightInKilograms) / (heightInMeters * heightInMeters)
Create a BMI calculator application that reads the user‟s weight in kilograms and height
in meters, then calculates and displays the user‟s body mass index. Also, the application 
should display the following information from the Department of Health and Human
Services/National Institutes of Health so the user can evaluate his/her BMI:
BMI VALUES
Underweight: less than 18.5
Normal: between 18.5 and 24.9
Overweight: between 25 and 29.9
Obese: 30 or greater"""



Weight=float(input("Enter weight in kg "))
Height=float(input("Enter height in meters : "))

BMI = round(Weight/(Height*Height),2)

if BMI<18.5:
    print("Underweight")
elif (BMI>=18.5) or BMI<=24.9:
    print("Normal")

elif (BMI>=25) or BMI<=29.9:
    print("Overweight")

elif (BMI>=30):
    print("Obese")