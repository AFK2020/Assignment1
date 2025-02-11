# property decorator =Decorator used to define a method as a property(it can be accessed like an attribute)
# Benefit: Add additional logoc when read, write, or delete attributes
# Gives you getter, setter, deleter nethod

class Rectangle:

    def __init__(self,width,height):
        self._width=width       #protected attribute
        self._height = height   #protected attribute

    @property       
    def width(self):       #getter method
        return f"{self._width:.1f}cm"
    
    @property
    def height(self):
        return f"{self.height: .1f}cm"
    
