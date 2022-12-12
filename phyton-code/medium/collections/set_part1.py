# A python Set is the collection of the unordered items
# Set is mutable (can be modified after its created)
# Element of set can not access directly by index
# display list of set by iterating through element

# create python set
colors = {"RED", "BLUE", "BLACK", "BROWN", "WHITE"}
# display set elements
print(colors)
# iterate through a set using for loop
for color in colors:
    print(color)
# get the type of colors
print(type(colors))

# set() METHOD, to initialize set
colors = set(["RED", "BLUE", "BLACK", "BROWN", "WHITE"])
print(colors)

# empty set
colors = set()
print(colors)

# add elements to set
colors.add("SILVER")
colors.add("RED")
print(colors)

# update the original set
colors.update(["WHITE"])
print(colors)

# removing elements from set using discard(), remove()
# colors.remove([0])  # you can't access set element by index
colors.remove("RED")
print(colors)
colors.discard("WHITE")
print(colors)

# union of two sets using '|' operator and union() method
even_number = set(["2", "4", "6"])
odd_number = set(["1", "3", "5"])
print(odd_number | even_number)
print(odd_number.union(even_number))

# intersection of two sets using '&' operator and intersection() method
even_number = set(["2", "4", "6"])
odd_number = set(["1", "2", "5", "4"])
print("integers: ", odd_number.intersection(even_number))

integer = odd_number & even_number
print("integers: ", integer)

# difference between two sets
even_number = set(["2", "4", "6"])
odd_number = set(["1", "2", "5", "4"])
difference = odd_number - even_number
print(difference)
difference = even_number - odd_number
print(difference)
print(even_number.difference(odd_number))
print(odd_number.difference(even_number))

# Symmetric difference of two sets, elements except the common of two sets
even_number = set(["2", "4", "6"])
odd_number = set(["1", "2", "5", "4"])
symmetric_number = even_number ^ even_number
symmetric_number2 = even_number.symmetric_difference(odd_number)
print(symmetric_number)
print(symmetric_number2)
