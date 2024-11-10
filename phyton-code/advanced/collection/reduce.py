"""
How does reduce() and filter() work in Python?

filter(): Filters elements from an iterable based on a function.
reduce(): Applies a function to the items of an iterable, cumulatively,
from left to right, to reduce the iterable to a single value.
Both functions are part of Python’s functools module (Python 3.x) and
can be used together to filter and then reduce data if needed.

The reduce(fun,seq) function is used to apply a particular function passed
in its argument to all the list elements mentioned in the sequence passed along.
This function is defined in “functools” module.

"""
# importing functools for reduce()
import functools
import operator

# 1. get the sum of the num_list elements
num_list = [3, 6, 7, 8]

print("The sum of the list element:", functools.reduce(lambda a, b: a + b, num_list))

# find the maximum element from the list
print("The maximum element form the list: ", functools.reduce(lambda a, b: a if a > b else b, num_list))

# python code to demonstrate working of reduce()
# using operator functions
print("Sum of elements in the list: ", functools.reduce(operator.add, num_list))
print("The product of elements in the list: ", functools.reduce(operator.mul, num_list))
