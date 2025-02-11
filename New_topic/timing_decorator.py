
import timeit
import functools



#repeat decorator
def repeat(number=2):

    def inner_repeat(func):

        @functools.wraps(func)
        def wrapper_repeat(*args,**kwargs):
            for i in range(number):
                func(*args,**kwargs)
        
        return wrapper_repeat

    return inner_repeat



#timer decorator

def timer(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start=timeit.timeit()
        func(*args,**kwargs)
        end=timeit.timeit()

        print(f"Time taken by {func.__name__} function is {end - start}")
    
    return wrapper

@timer
@repeat(10)
def print_function(x):
    print(x)


string1= "Hello! Afifa"
print_function(string1)