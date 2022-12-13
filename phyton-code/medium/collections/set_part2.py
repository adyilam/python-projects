# set comparison
color_set1 = set({"RED", "BLUE", "BLACK", "YELLOW"})
color_set2 = set({"BLACK", "YELLOW"})
print(color_set1 > color_set2)  # color_set1 is a superset of color_set2, return true
print(color_set2 > color_set1)  # false

color_set3 = set({"BLACK", "YELLOW"})
print(color_set2 == color_set3)  # true

# python frozen set - is immutable set, once its created it can't be able to modify
# the elements of frozen set can't be modified, it can be used as key in python dictionary
frozen_set = frozenset([1, 2, 3, 4])
print(type(frozen_set))
# print(frozen_set)

for i in frozen_set:
    print(i)
# try to add one element, this will throw error
# frozen_set.add(5)

# remove a specific element of set of numbers based on user choice
numbers = {1, 2, 3, 4, 5, 6}
print("Numbers before removed", numbers)
user_choice = int(input("Enter the number to be removed: "))
numbers.discard(user_choice)
print("Numbers After removed", numbers)
