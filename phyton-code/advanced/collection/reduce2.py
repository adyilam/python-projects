"""
Both reduce() and accumulate() can be used to calculate the summation of a sequence elements.
But there are differences in the implementation aspects in both of these.

reduce() is defined in “functools” module, accumulate() in “itertools” module.
reduce() stores the intermediate result and only returns the final summation value.
Whereas, accumulate() returns a iterator containing the intermediate results.
The last number of the iterator returned is summation value of the list.
reduce(fun, seq) takes function as 1st and sequence as 2nd argument.
In contrast, accumulate(seq, fun) takes sequence as 1st argument and function as 2nd argument.
"""

# importing itertools for accumulate()
import itertools

# importing functools for reduce()
import functools

# initializing list
num_list = [1, 3, 4, 10, 4]
print("The sum of elements in the list using accumulate: ", list(itertools.accumulate(num_list, lambda x, y: x + y)))
print("The sum of elements in the list using reduce:", functools.reduce(lambda x, y: x + y, num_list))
