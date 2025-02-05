#The distance between two cities (in km.) is input through the keyboard. Write a program
#to convert and print this distance in meters, feet, inches and centimeters.

distance= int(input("Enter distance in km"))

distance_meters=distance*1000
distance_feet=distance*3280.84
distance_inches=distance*39370.1
distance_cm=distance_meters*100

print("Distance in meters",distance_meters,"m")
print("Distance in feet",distance_feet,"ft")
print("Distance in inches",distance_inches,"in")
print("Distance in centimeters",distance_cm,"cm")