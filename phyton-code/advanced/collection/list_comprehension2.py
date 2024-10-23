# syntax: [expression for item in iterable if condition] if condition(optional)
# iterate through given list and return another list with a square of each element
# using for loop
nums = [1, 2, 3, 4, 5]

# Create an empty list 'res' to store results
result = []

# Iterate over each element in list 'nums'
for val in nums:
    # Multiply each element by 2 and append it to 'result'
    result.append(val * 2)

print(result)

# using list comprehension
result = [val * 2 for val in nums]

print(result)

# using list comprehension with conditional statement
result = [val * 2 for val in nums if val % 2 == 0]

print(result)

# nested loop
# Creates a list of tuples representing all combinations of (x, y)
# where both x and y range from 0 to 2.
coordinates = [(x, y) for x in range(3)
               for y in range(3)]

print(coordinates)

# Flattening a list of lists
mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

res = [val for row in mat for val in row]

print(res)

# below list contains square of all odd numbers from
# range 1 to 10
odd_square = [x ** 2 for x in range(1, 11) if x % 2 == 1]
print(odd_square)

# using for loop
odd_square = []
for x in range(1, 11):
    if x % 2 == 1:
        odd_square.append(x ** 2)
        print(odd_square)

# below list contains power of 2 from 1 to 8
power_of_2 = [2 ** x for x in range(1, 9)]
print(power_of_2)

# list only power of odd numbers else multiply by 2
power_of_2 = [2 ** x if x % 2 == 1 else x * 2 for x in range(1, 11)]
print(power_of_2)

# using loop
power_of_2 = []
for x in range(1, 11):
    if x % 2 == 1:
        power_of_2.append(2 ** x)
    else:
        power_of_2.append(x * 2)
print(power_of_2)

# print multiplication table
print("Multiplication Table: ")
a = 6
multi_table = [[a, b, a * b] for b in range(1, 5)]
# print(multi_table)

# display multiplication table
for i in multi_table:
    print(i)

# Division table
print("Division Table: ")
a = 2
div_table = [[a, b, a / b] for b in range(1, 5)]
for i in div_table:
    print(i)

# slicing
#  below list has numbers from 6 to 8
lst = list(range(1, 11))
lst5_8 = lst[5: 8]
print(lst5_8)

#  below list has numbers from 2 to 10
lst1_ = lst[1:]
print(lst1_)

#  below list has numbers from 1 to 5
lst_5 = lst[: 5]
print(lst_5)

#  below list has numbers from 2 to 8 in step 2
lst1_8_2 = lst[1: 8: 2]
print(lst1_8_2)

#  below list has numbers from 10 to 1
lst_rev = lst[:: -1]
print(lst_rev)

#  below list has numbers from 10 to 6 in step 2
lst_rev_9_5_2 = lst[9: 4: -2]
print(lst_rev_9_5_2)
