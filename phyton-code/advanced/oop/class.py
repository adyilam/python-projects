"""
Syntax: Class Definition
class ClassName:
    # Statement

Syntax: Object Definition

obj = ClassName()
    # Statement

Some points on Python class:

Classes are created by keyword class.
Attributes are the variables that belong to a class.
Attributes are always public and can be accessed using the dot (.) operator. Eg: My class.Attribute

"""


class MyClass:
    def __init__(self, att):
        self.att = att


att = "Hello there!!"
obj = MyClass(att)
print(obj.att)


# class Dog
class Car:
    # Class Variable
    vehicle = 'car'

    # init method or constructor
    def __init__(self, color, model):
        # Instance Variable
        self.color = color
        self.model = model

    # Sample Method
    def function(self):
        print(self.color)
        print(self.model)


# Object of Car class, BMW
BMW = Car("white", "X4")

# Accessing class attributes
# and method through objects
print(BMW.color, BMW.model)
BMW.function()

# calling class variable using Car
print("value of class variable: ", Car.vehicle)
