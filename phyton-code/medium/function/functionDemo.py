# python function syntax
# def function_name(parameters):
"""the block of code goes below"""
from unittest import result


# code block

# calling a function
def greetings(string):
    return string


print("Greetings : ", greetings("hello there!!"))


# user-defined function
def area_circle(radius):
    return 3.14 * radius ** 2


def area_rectangle(length, width):
    return length * width


# call different functions
area_of_a_circle_ = area_circle(2)
area_of_a_rectangle_ = area_rectangle(2, 3)
print("The area of a circle is: ", area_of_a_circle_)
print("The area of a rectangle is: ", area_of_a_rectangle_)


# handling exception
def add(num1, num2):
    return num1 * num2


print("passing one argument to add() function ")
try:
    add(2)
except:
    print("Error: function takes two argument!!")


# variable length arguments
# "args" and "kwargs" refer to arguments not based on keywords.
def employees_name(*args_list):
    name = []
    for i in args_list:
        name.append(i.upper())
        return name


print("Employees list: ")
employee_names = employees_name('Alex smith', 'Marta ben', 'Tom cruise')
print(employee_names)


# defining a function
def employees(**kwargs_list):
    name = []
    for key, value in kwargs_list.items():
        name.append([key, value])
        return name


print("Employees list: ")
# Passing kwargs arguments
names = employees(One="Alex smith", Two="Marta ben", Three="Tom cruise")
print(names)

# Anonymous function
# The lambda keyword can define anonymous, short, single-output functions
# syntax
# lambda [argument1 [,argument2... .argument n]] : expression

# define anonymous function
lambda_ = lambda length, width: length + width
print("Anonymous function call: ", lambda_(5, 6))


# How to access variables of nested function
def nested_function():
    message = 'Pages printed >>>'
    pages = 2

    def printer():
        print(message)
        print(pages)

    printer()


nested_function()

# Python built-in functions
# abs(), all(),bin(), bytes(), callable(), compile(), exec(), sum(), any(), ascii()
# bytearray(), eval(), float(), format(), frozenset(), getattr(), globals(), hasattr()
# iter(), len(), list(), locals(), map(),memory(), object(), open(), chr(), complex()
# delattr(), dir(), div-mod(), enumerate(), dict(), filter(), hash(), help(), min()
# set(),  hex(), id(), setattr(), slice(), sorted(), next(), input(), int(), isinstance()
# oct(), ord(), pow(), print(), range(), reversed(), round(), issubclass(), tuple(), type(),
# vars(), zip()

# abs() function
number = -20
print("Absolute value of ", number, "is:  ", abs(number))

# all() function, accepts an iterable object (such as list, dictionary, etc.)
# It returns true if all items in passed iterable are true. Otherwise, it returns False.
value = [2, 4, 5, 9]
print(all(value))

value1 = [0, 1, 2]
print(all(value1))

value2 = [False, 0]
print(all(value2))

# empty value iterable
value3 = []
print(all(value3))

# bool() function, converts a value to boolean(True or False) using the standard truth testing procedure.
number = 10
print(number, " is: ", bool(number))

number1 = []
print(number1, " is: ", bool(number1))

number2 = True
print(number2, " is: ", bool(number2))

number3 = None
print(number3, " is: ", bool(number3))

# exec() function, exec() function is used for the dynamic execution of Python program which can either be
# a string or object code, and it accepts large blocks of code,
# unlike the eval() function which only accepts a single expression.
numbers = [2, 3, 7, 4, 8]
result1 = sum(number * 2 for number in numbers if number % 2 == 0)
print(result1)

# one line code using exec() function
exec("result = sum(number*2 for number in numbers if number % 2 == 0)")
print(result)

# factorial() will be executed
from math import *

exec("print(factorial(5))", {"factorial": factorial})

# an exception will be raised
exec("print(factorial(5))", {})  # NameError: name 'factorial' is not defined


# filter() function is used to get filtered elements. This function takes two arguments,
# first is a function and the second is iterable.
def filterNumbers(num):
    if num > 1:
        return num


# calling filterNumber()
value = filter(filterNumbers, (2, 3, 4))
# print value
print(list(value))
