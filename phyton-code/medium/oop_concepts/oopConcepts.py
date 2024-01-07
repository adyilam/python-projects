# class can be defined as a collection of objects.
# It is a logical entity that has some specific attributes and methods.
'''
Syntax:
class className:
    <expression1>
        ...
    <expressionN>
'''


# Object - is an entity that has state and behavior.
# declaring an object phone
# object_name = Class_Name(arguments)

# constructor -  constructor is called automatically when we create the object of the class
# non-parametrized constructor
class Product:
    # Constructor - non parameterized
    def __init__(self):
        print("This is non parametrized constructor")

    def show(self, name):
        print("Product name is: ", name)


product = Product()
product.show("Cloth")


# Parameterized Constructor
class Product:
    # Constructor - parameterized
    def __init__(self, name):
        print("This is parametrized constructor")
        self.name = name

    def show(self):
        print("Product name is: ", self.name)


product = Product("TV")
product.show()


# default constructor
class Book:
    isbn = 101
    name = "Architecture"

    def display(self):
        print("Book info:  ", "isbn- ", self.isbn, ", name- ", self.name)


book = Book()
book.display()


class phone:
    count = 0  # a class variable

    def __init__(self, model, version):
        self.model = model  # instance variable
        self.version = version
        phone.count += 1  # accessing the class variable with the name of the class

    def show(self):
        print(self.model, self.version)


# calling a method that is also the name of the property
class Book:
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn

    def get_isbn(self):
        return self.isbn


isbn = {'isbn10': '1492051292', 'isbn13': '978-1492051299'}
book = Book('Head First Python', isbn)

print(book.get_isbn())
# creating instance of the object phone and assign the value to variable phone1
phone1 = phone("iphone", 14)
phone2 = phone("Android", 12)
phone1.show()
print(phone.count)


# accessing attributes using getattr()
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary


# creating the Employee object
emp = Employee("Alex", 33, "$10k")
print(getattr(emp, 'name'))

# reset the attribute value of name using setattr()
setattr(emp, "name", "Tom")
# print updated name
print(getattr(emp, 'name'))
# check the attribute in object if exist return true,
print(hasattr(emp, 'name'))
print(hasattr(emp, 'id'))
# delete the attribute from the object
delattr(emp, 'salary')
# check the deleted attribute
# print(emp, emp.salary)  # AttributeError: 'Employee' object has no attribute 'salary'

# method is a function that is associated with an object.
# In Python, a method is not unique to class instances.
# Any object type can have methods.

# Inheritance - one of the concept of oop,
# It specifies that the child object acquires all the properties and behaviors of the parent object.
'''
class derive-class(<base class 1>, <base class 2>, ..... <base class n>):  
    <class - suite> 
'''


class Person:
    def getPersonInfo(self):
        print("Person information")


class Employee(Person):  # child class Employee inherits the base class Person
    def getEmplyeeInfo(self):
        print("Employee information")


d = Employee()
d.getEmplyeeInfo()
d.getPersonInfo()

# issubclass(sub, sup) method is used to check the relationships between the specified classes.
# returns true if the first class is the subclass of the second class, and false otherwise.
print("Is Employee a subclass of Person:  ", issubclass(Employee, Person))

# isinstance() method is used to check the relationship between the objects and classes.
# It returns true if the first parameter, i.e., obj is the instance of the second parameter, i.e., class.
employeeInfo = Employee()
list_ = [1, 2, 3, 4]
print("Is it Employee instance: ", isinstance(employeeInfo, Employee))
print("Is it Employee instance: ", isinstance(list_, Employee))


# When the parent class method is defined in the child class with some specific implementation,
# then the concept is called method overriding.

class Person:
    def work(self):
        print("Person work")


class Employee(Person):  # child class Employee inherits the base class Person
    def work(self):  # overrides method in Person
        print("Employee work")


d = Employee()
d.work()

# Abstraction is used to hide the internal functionality of the function from the users.
# The users only interact with the basic implementation of the function, but inner working is hidden.
# Python program to define
# abstract class

from abc import ABC


class Shape(ABC):

    # abstract method
    def area(self):
        pass


class Triangle(Shape):

    def area(self):
        print("Area of a Triangle")


class Rectangle(Shape):

    def area(self):
        print("Area of a Rectangle")


class Circle(Shape):

    def area(self):
        print("Area of a Circle")


# Driver code
t = Triangle()
t.area()

s = Rectangle()
s.area()

p = Circle()
p.area()
