"""
Benefits of inheritance are:
Inheritance allows you to inherit the properties of a class, i.e., base class to another, i.e., derived class.
The benefits of Inheritance in Python are as follows:

It represents real-world relationships well.
It provides the reusability of a code. We don’t have to write the same code again and again. Also, it allows us to add more features to a class without modifying it.
It is transitive in nature, which means that if class B inherits from another class A, then all the subclasses of B would automatically inherit from class A.
Inheritance offers a simple, understandable model structure.
Less development and maintenance expenses result from an inheritance.

Syntax:
Class BaseClass:
    {Body}
Class DerivedClass(BaseClass):
    {Body}
"""


# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Animal sound"


# Child class that inherits from Animal
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call parent class constructor
        self.breed = breed

    def speak(self):
        return f"{self.name} says Woof!"


# Create an object of the Dog class
dog = Dog("Alex", "German Shepherd")

# Access attributes and methods
print(dog.name)  # Inherited from Animal
print(dog.breed)  # Defined in Dog
print(dog.speak())  # Overridden method in Dog
