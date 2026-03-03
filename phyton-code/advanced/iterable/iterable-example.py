"""
Iterable:
    An object capable of returning its members one at a time (e.g., lists, strings, tuples).
    method: Implements the __iter__() method, which returns an iterator.
    ReUsability : Can be iterated over multiple times.
    Relationship: Every iterator is an iterable, but not every iterable is an iterator.

Iterator:
    An object with a state that produces the next value each time it is requested.
    Method: Implements both the __iter__() method (which returns self) and the __next__() method.
    ReUsability: Can only be used once (it gets exhausted after a single pass).
    Relationship: A subset of iterables that maintain iteration state.

=> An iterable is any object that can return an iterator,
   while an iterator is the actual object that performs iteration one element at a time.

Custom Iterator :
    Creating a custom iterator in Python involves defining a class that implements
    the __iter__() and __next__() methods according to the Python iterator protocol.
"""
# iterator vs iterable example

# Iterable: list
numbers = [1, 2, 3]

# Iterator: created using iter()
it = iter(numbers)
print(next(it))
print(next(it))
print(next(it))

# An iterable: a list of numbers
my_list = ["Abc", "Def", "Hij"]

# The list itself is not an iterator; calling next() on it raises a TypeError
try:
    next(my_list)
except TypeError as e:
    print(f"Error: {e}")  # Output: Error: 'list' object is not an iterator

# Create an iterator from the iterable using the built-in iter() function
my_iterator = iter(my_list)

# An iterator: you can get the next item using the built-in next() function
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))

# Once exhausted, the iterator raises a StopIteration exception
try:
    next(my_iterator)
except StopIteration:
    print("The iterator is exhausted.")  # Output: The iterator is exhausted.


# Custom Iterator
class OddNumbers:
    def __iter__(self):
        self.n = 1  # Start from the first odd number
        return self

    def __next__(self):
        x = self.n
        self.n += 2  # Increment by 2 to get the next odd number
        return x


# Create an instance of oddNumbers
odd = OddNumbers()
it = iter(odd)

# Print the first five odd numbers
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

# StopIteration Exception
list_ = [2, 4, 6, 8, 10]
itr = iter(list_)

while True:
    try:
        print(next(itr))
    except StopIteration:
        print(f"The iteration ended")
        break

# Option1, accessing each value of a list with index
my_list = ['tv', 'speaker', 'computer']
i = 0
while i < len(my_list):
    print(f"Index: {i}, Value: {my_list[i]}")
    i += 1

# Option2, accessing each value of a list with index
my_list = ['tv', 'speaker', 'computer']
for i in range(len(my_list)):
    print(f"Index: {i}, Value: {my_list[i]}")
