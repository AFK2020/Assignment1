

student_data = []

for i in range(5):  
    name = input("Enter name: ")
    marks = int(input("Enter marks: "))
    
    student_data.append(name)  # Name at even index
    student_data.append(marks)  # Marks at odd index


print("The final list is:", student_data)