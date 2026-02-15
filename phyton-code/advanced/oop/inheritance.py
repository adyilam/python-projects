"""
Benefits of inheritance are:

Inheritance allows you to inherit the properties of a class, i.e., base class to another,
i.e., derived class. The benefits of Inheritance in Python are as follows:

- It represents real-world relationships well.
- It provides the re-usability of a code. We don’t have to write the same code again and again. Also,
- It allows us to add more features to a class without modifying it.
- It is transitive in nature, which means that if class B inherits from another class A, then all
  the subclasses of B would automatically inherit from class A.
- Inheritance offers a simple, understandable model structure.
- Less development and maintenance expenses result from an inheritance.

Python Inheritance Syntax:
The syntax of simple inheritance in Python is as follows:

Class BaseClass:
    {Body}
Class DerivedClass(BaseClass):
    {Body}

"""


# 1. creating parent class
class Animal(object):
    # constractor
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    # method
    def make_sound(self):
        print(self.name, self.sound)


# object of Animal
cat = Animal("kitty", "Meow")
cat.make_sound()


# 2. create a child class
class Dog(Animal):

    def show(self):
        print("Dog class invoked")


# create Dog instance
dog = Dog("Alex", "woof")

# calling parent class function
dog.make_sound()

# calling a child class function
dog.show()
