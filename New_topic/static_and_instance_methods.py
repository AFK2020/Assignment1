
class Employee:

    def __init__(self,name,position):
        self.name= name
        self.position =position
    
    def get_info(self): #instance method because each object(instance of the class) will have it's own
        return f"{self.name} = {self.position}"                    #get info method


    @staticmethod       #we need decorator for static method
    def is_Valid(position): #static method doesn't take self argument because it does not need an object to work
        valid_positions= {"manager", "cook" , "cashier", "waiter", "janitor"}

        return position in valid_positions
    
employee1= Employee("Eugene", "Manager")    #instance of class

print(employee1.get_info())         #calling instance method

print(Employee.is_Valid("manager"))