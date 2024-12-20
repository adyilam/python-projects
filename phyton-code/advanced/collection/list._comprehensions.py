# List Comprehensions creates a new list from range 1 to 10
list_ = []
for i in range(1, 10):
    list_.append(i)

print(list_)

# the above logic, using list Comprehensions,  in a single, readable line.
list_comp = [i for i in range(1, 10)]
print(list_comp)

# Using a list comprehension, create a new list called "newlist"
# out of the list "numbers", which contains only the positive numbers from the list, as integers.
numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
newlist = []
list_compr = [newlist for newlist in numbers if newlist >= 0]
print(list_compr)

# 5x5 matrix
matrix = []
for i in range(5):
    # Append an empty sublist inside the list
    matrix.append([])
    for j in range(5):
        # populates each sublist with values ranging from 0 to 4
        matrix[i].append(j)
print(matrix)
