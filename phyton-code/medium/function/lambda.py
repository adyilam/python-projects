# Lambda Functions in Python are anonymous functions,function don't have a name
# Lambda keyword in Python to define an unnamed function. like def keyword  used to
# create python function
# syntax  lambda arguments: expression
def multiply(x, y):
    return x * y


print(multiply(2, 3))

# multiply function using lambda
value = lambda x, y: (x * y)
print(value(4, 5))

# filter even numbers from the list of integers, using filter()
list_ = [2, 4, 5, 6, 7, 8, 9]
odd_numbers = list(filter(lambda n: (n % 2 == 0), list_))
print("List of odd numbers: ", odd_numbers)

# find the square of numbers in the list using map()
list_ = [2, 4, 5, 6, 7, 8, 9]
square_of_a_number = list(map(lambda n: (n * 2), list_))
print("The square of the number ", list_, " is:   ", square_of_a_number)

# lambda function combined with list comprehension and the lambda keyword with a for loop.
squares_of_each_number = [lambda num=num: num ** 2 for num in range(0, 11)]
print('The square value of all numbers from 0 to 10:')
for square in squares_of_each_number:
    print(square(), end=" ")

# lambda with if else condition
is_odd_ = lambda x: True if (x % 2 != 0) else False
print("\n Is it odd number: ", is_odd_(6))
