"""
Polymorphism: refers to ability of the same method or operation to behave differently based on object.
It mainly includes compile-time and runtime polymorphism.

compile-time: means deciding which method or operation to run during compilation,
usually through method or operator overloading. using default and variable-length arguments.

runtime polymorphism: using Method Overriding a child class provides its own version of a method already defined in the parent class

"""


# compile time polymorphism
class Calculator:
    def addation(self, x=1, y=1, *args):
        value = x + y
        for i in args:
            value *= i
        return value


cal = Calculator

# using default arguments
print(cal.addation(1))
print(cal.addation(2))

# using multiple arguments
print(cal.addation(2, 4))
print(cal.addation(3, 4, 5))


# runtime polymorphism

class Animal:
    def sound(self):
        return "Some generic sound"


class Dog(Animal):
    def sound(self):
        return "Bark"


class Cat(Animal):
    def sound(self):
        return "Meow"


# Polymorphic behavior
animals = [Dog(), Cat(), Animal()]
for animal in animals:
    print(animal.sound())
