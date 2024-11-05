"""
You can access values in the nested list using indexing.
Each item in the outer list is itself a list,
so you need two indices: one for the outer list and one for the inner list.

Just specify the outer list index first (like nested_list[1]),
and then the inner list index (like nested_list[1][1]).
"""

nested_list = [['blue', 'green'], ['red', 'black'], ['blue', 'white']]
print(len(nested_list))  # size of the list
# 1. Accessing entire inner lists
print(nested_list[0])  # outer loop index 0
print(nested_list[1])  # outer loop index 1
print(nested_list[2])  # outer loop index 2

# 2. Accessing individual items in inner lists
# Access the first item in the first inner list
print(nested_list[0][0])  # Output: 'blue'
# Access the second item in the second inner list
print(nested_list[1][1])  # Output: 'black'
# Access the first item in the third inner list
print(nested_list[2][0])  # Output: 'blue'

# 3. Looping through each element
print("== looping through each element == ")
for inner_list in nested_list:
    for color in inner_list:
        print(color)

# how to access and compare values in this list of lists
# Let's say we want to find and print the sublist that contains 'black'
for sublist in nested_list:
    if 'black' in sublist:
        print("Found 'black' in sublist: {sublist}")

# Or, if you want to find a specific combination, like ['blue', 'white']
for sublist in nested_list:
    if sublist == ['blue', 'white']:
        print("Found the exact match:", sublist)
