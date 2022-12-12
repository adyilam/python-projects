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
