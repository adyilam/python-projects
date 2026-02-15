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


# 1. single inheritance
class Animal:
    def __init__(self, name):
        self.name = name


class Dog(Animal):  # Dog inherits from Animal
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed


# Creating an instance of the Dog class
dog = Dog("jack", "Shepperd")
print(dog.name)
print(dog.breed)


# 2. multiple inheritances- a child class can inherit from more than one parent class
# Python example to show the working of multiple
# inheritance

class Animal(object):
    def __init__(self):
        self.name1 = "Animal"
        print("Animal class")


class Dog(object):
    def __init__(self):
        self.name2 = "Dog"
        print("Dog class")


class Cat(Animal, Dog):  # inherit from both Animal and Dog
    def __init__(self):
        # Calling constructors of Animal
        # and Base2 classes
        Animal.__init__(self)
        Dog.__init__(self)
        print("Derived")

    def printname(self):
        print(self.name1, self.name2)


ob = Cat()
ob.printname()


# 3. multilevel Inheritance- a class is derived from another derived class.
class Animal:
    def __init__(self, name):
        self.name = name


class Cat(Animal):
    def sound(self):
        print(self.name, "is an animal")


class Dog(Cat):
    def classification(self, classification):
        print(self.name, "is: ", classification)


dog = Dog("Type")
dog.sound()
dog.classification("Carnivorous")


# 4. hierarchical inheritance - multiple child classes inherit from the same parent class.
class Animal:
    def __init__(self, name):
        self.name = name


class Cat(Animal):
    def sound(self):
        print(self.name, ": is sound of a Cat")


class Dog(Animal):
    def sound(self):
        print(self.name, ": is sound of a Dog")


cat = Cat("meows")
cat.sound()

dog = Dog("woof")
dog.sound()
