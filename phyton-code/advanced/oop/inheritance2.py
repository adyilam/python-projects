"""
What Are the Different Types of Inheritance?

Python supports multiple types of inheritance:
1. Single Inheritance: A child class inherits from a single parent class.

class Parent:
    pass

class Child(Parent):
    pass
2. Multiple Inheritance: A child class inherits from more than one parent class.

class Parent1:
    pass

class Parent2:
    pass

class Child(Parent1, Parent2):
    pass
3. Multilevel Inheritance: A child class inherits from a parent class, which in turn inherits from another parent class.

class Grandparent:
    pass

class Parent(Grandparent):
    pass

class Child(Parent):
    pass
4. Hierarchical Inheritance: Multiple child classes inherit from the same parent class.

class Parent:
    pass

class Child1(Parent):
    pass

class Child2(Parent):
    pass

5. Hybrid Inheritance: A combination of two or more types of inheritance.


class Parent1:
    pass

class Parent2:
    pass

class Child1(Parent1):
    pass

class Child2(Parent1, Parent2):
    pass

How to Use super() in Python?

...
The super() function is used to call a method from the parent class.
It is commonly used to invoke the parent class’s __init__ method from
the child class to ensure proper initialization.

"""


class Animal:
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed


# Creating an instance of the Dog class
dog = Dog("jack", "Shepperd")
print(dog.name)
print(dog.breed)
