# map() function returns a map object which is an iterator(list, tuple etc.)
# Syntax: map(fun, iter)
# Parameters:
# fun: It is a function to which map passes each element of given iterable.
# iter: It is iterable which is to be mapped.

# get the square of the given list of numbers
def square(x):
    return x * x


nums = (3, 4, 5, 6, 7)
value = map(square, nums)
print(list(value))

# get the square of the given list of numbers, using lambda
nums = (3, 4, 5, 6, 7)
result = map(lambda x: x * x, nums)
print(list(result))

# combining two lists using map
list1_ = (1, 2, 3, 4)
list2_ = (5, 6, 7, 8)
result1 = map(lambda x1, x2: x1 + x2, list1_, list2_)
print(list(result1))


# print the square of even numbers from the given list, map
def square(x):
    if x % 2 != 0:
        return x
    else:
        return x * x


nums = (2, 3, 4, 5)
square_of_a_number = map(square, nums)
