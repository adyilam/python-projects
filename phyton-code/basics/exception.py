"""
Exceptions

Errors detected during execution are called exceptions.
Examples:
ZeroDivisionError
This error is raised when the second argument of a division or modulo operation is zero.

ValueError
This error is raised when a built-in operation or function receives an argument that has the right type but an inappropriate value.


Handling Exceptions

The statements try and except can be used to handle selected exceptions.
A try statement may have more than one except clause to specify handlers for different exceptions.

Syntax:
    try:
        # Code that might raise an exception
    except ExceptionType:
        # Code to handle the exception
    finally:
        # Code that will always be executed
"""
# ZeroDivisionError: integer division or modulo by zero
a = '1'
b = '0'
print(int(a) / int(b))

# ValueError: invalid literal for int() with base 10: '#'
a = '1'
b = '#'
print(int(a) / int(b))

# Exception
try:
    print(1 / 0)
except ZeroDivisionError as e:
    print("Error Code:", e)
