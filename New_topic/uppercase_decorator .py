#Basic Decorator:
#Create a decorator called @uppercase_decorator that converts the result of a
#function to uppercase. Apply this decorator to a function that returns a string and test it.


import functools

def upper_case_decorator(func):

    @functools.wraps(func)
    def wrapper():
        return func().upper()
    
    return wrapper


@upper_case_decorator
def greet():
    return "Hello! World"


print(greet())


