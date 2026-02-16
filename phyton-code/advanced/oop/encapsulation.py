"""
Encapsulation is one of the fundamental concepts in object-oriented programming (OOP).
It describes the idea of wrapping data and the methods that work on data within one unit.
This puts restrictions on accessing variables and methods directly and can prevent the accidental modification of data.

Encapsulation:
Definition: The bundling of data and methods that operate on the data into a single unit, with controlled access to the internal state.
Purpose: To protect an object’s internal state and expose a controlled interface.
Implementation: Achieved through private and protected members.

Abstraction:
Definition: The concept of hiding complex implementation details and showing only the essential features of an object.
Purpose: To simplify interaction with objects by focusing on high-level operations rather than implementation details.
Implementation: Achieved through abstract classes and methods, interfaces, and high-level class design.

"""


class Person:

    def __init__(self, name, age):
        self.name = name  # public attribute
        self.__age = age  # private attribute , by keeping__age variable private inside Person class.

    def show_age(self):  # using a public method to access a private attribute __age
        print("Age: ", self.__age)


per = Person("Samuel", 23)
print(per.name)
# private members cannot be accessed directly from outside the class.
# print(per.__age)    # this show an issue, because __age is private attribute.
per.show_age()
