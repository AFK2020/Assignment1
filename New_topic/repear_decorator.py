#Parameterised Decorator:
#Create a decorator @repeat(n) that repeats the decorated function n times. It should also accept an argument for whether to print the results each time. 
#Apply this decorator to a simple function.

import functools

def repeat(number=2):

    def inner_repeat(func):

        @functools.wraps(func)
        def wrapper_repeat(*args,**kwargs):
            for i in range(number):
                func(*args,**kwargs)
        
        return wrapper_repeat

    return inner_repeat


@repeat(5)
def print_function(x):
    print(x)


string1= "Hello! Afifa"
print_function(string1)