#Write a program that takes the marks obtained by a student in five different subjects as
#input through the keyboard, then find out the total marks and percentage marks obtained
#by the student in each subject. Assume that the maximum marks that can be obtained by a
#student in each subject is 100.

print("Enter Marks obtained")

Maths=int(input("Maths"))
Physics=int(input("Physics"))
Chemistry=int(input("Chemistry"))
Thermodynamics=int(input("Thermodynamics"))
ITC=int(input("Intro to Computing"))

Total_marks=Maths+Physics+Chemistry+Thermodynamics+ITC
print("Total Marks=",Total_marks,"/500")
print("Percantage=", (Total_marks/500)*100,"%")