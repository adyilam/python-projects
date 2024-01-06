# class can be defined as a collection of objects.
# It is a logical entity that has some specific attributes and methods.
'''''
Syntax:
class className:
    <expression1>
        ...
    <expressionN> 
'''''


# Object - is an entity that has state and behavior.
# declaring an object phone
# object_name = Class_Name(arguments)
class phone:
    count = 0  # a class variable

    def __init__(self, model, version):
        self.model = model  # instance variable
        self.version = version
        phone.count += 1  # accessing the class variable with the name of the class

    def show(self):
        print(self.model, self.version)


# creating instance of the object phone and assign the value to variable phone1
phone1 = phone("iphone", 14)
phone2 = phone("Android", 12)
phone1.show()
print(phone.count)


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


# method is a function that is associated with an object.
# In Python, a method is not unique to class instances.
# Any object type can have methods.

# Inheritance - one of the concept of oop,
# It specifies that the child object acquires all the properties and behaviors of the parent object.
