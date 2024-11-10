"""
Filter Function in Python with Lambda and Custom Function
problem : Use filter and a lambda function to
          filter the list of numbers and only
          keep the ones that are multiples of 2
          ...
Time complexity analysis:

The filter function is used to filter the list of numbers, and it applies the lambda function to each element of the list.
The time complexity of the filter function is O(n), where n is the number of elements in the list.
The time complexity of the lambda function is constant, O(1), since it only performs a single arithmetic operation.
Therefore, the overall time complexity of the program is O(n).
"""

# define a list of numbers
numbers = [1, 4, 6, 8, 9, 2, 10, 21]

# 1. using for loop only
result = []
for num in numbers:
    if num % 2 == 0:
        result.append(num)
        print("using for loop: ", result)

# 2. using list comprehension
result = [num for num in numbers if num % 2 == 0]
print("using list comprehension: ", result)


# 3. using lambda, filter function,
# function to check if number id multiple of three
def is_multiple_of_two(number):
    return number % 2 == 0


result = list(filter(lambda n: is_multiple_of_two(n), numbers))  # with custom function
# result = list(filter(lambda n: n % 2 == 0, numbers))

print("using filter & lambda function: ", result)
