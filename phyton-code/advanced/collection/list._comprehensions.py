# List Comprehensions creates a new list based on another list, in a single, readable line.
list_ = []
for i in range(1, 10):
    list_.append(i)

print(list_)

# the above logic, using list Comprehensions
list_comp = [i for i in range(1, 10)]
print(list_comp)

# Using a list comprehension, create a new list called "newlist"
# out of the list "numbers", which contains only the positive numbers from the list, as integers.
numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
newlist = []
list_compr = [newlist for newlist in numbers if newlist >= 0]
print(list_compr)
