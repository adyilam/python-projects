"""
A nested list is a list that contains another list (i.e.: a list of lists).
It is also referred to as a multidimensional array.
For example, a 2-dimensional array is used below:
"""
nested_list = [['blue', 'green'], ['red', 'black'], ['blue', 'white']]
print(len(nested_list))
# prints 3
print(nested_list[1])
# prints ['red', 'black']
print(nested_list[1][0])
# prints red

# To go through every element in this list, use a nested for loop.
for inner in nested_list:
    for value in inner:
        print(value)

# filtering the values to display only red and black colors else prnt space
for inner in nested_list:
    for value in inner:
        if (value == "red") | (value == "black"):
            print(value)
        else:
            print("")

# filter all even numbers from the given list of numbers using list comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

odd_numbers = []
for row in matrix:
    for element in row:
        if element % 2 == 0:
            odd_numbers.append(element)

print(odd_numbers)

#
records = [["chi", 20.0], ["beta", "50.0"], ["alpha", 50.0]]
temp = records[0]
for row in records:
    for value in row:
        print(value)

