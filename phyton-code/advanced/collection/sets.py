# Set: Sets are lists with no duplicate entries.

# set removes duplicate words from the given list.
list_ = ["test1", "test2", "test3", "test2"]
print(set(list_))

# get unique words from the given list of words
words = "This is a test words to show set in python set in python"
print(set(words.split()))

# Sets also helps to calculate differences and intersections between other sets.
# get the intersaction of x and y
x = set(["John", "Smith", "Marry"])
y = set(["Tom", "Abebe", "Smith"])
print(x.intersection(y))
print(y.intersection(x))

# get the elements of x and y exclude the intersection
print(x.symmetric_difference(y))
print(y.symmetric_difference(x))

# get elements only in each list exclude the intersection
print(x.difference(y))
print(y.difference(x))

# get the list of all elements of x and y
print(x.union(y))
print(y.union(x))
