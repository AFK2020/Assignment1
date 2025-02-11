
class Student:
    count=0     #class variable

    def __init__(self,name,gpa):
        self.name=name
        self.gpa=gpa
        
        Student.count+=1

    #Instance method
    def get_info(self):
        return f"{self.name} = {self.gpa}"
    
    @classmethod
    def get_count(cls):     #class method takes cls as first parameter
        return f"Total number of students = {cls.count}"
        

student1= Student("Spongebob", 3.2)
student2=Student("Afifa", 3.16)
student3= Student("Shery", 3.8)

print(Student.get_count())
