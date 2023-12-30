# A collection of ordered and immutable objects is known as a tuple.
# Tuples and lists are similar as they both are sequences.
# Tuples can not modify, but we can modify list after created
# When we create Tuples used parenthesis, List used square brackets

# how to create tuple in different types and forms
activity_tuple_string = ("Music", "Movie", "Sport")
int_tuple = (10, 20, 30)
activity_tuple_string_no_parenthesis = "Music", "Movie", "Sport"
empty_tuple = ()
print(activity_tuple_string, int_tuple, activity_tuple_string_no_parenthesis, empty_tuple)

tuples = "Computer", "Water", 55, 10, ["Food", "Books"]
print(tuples)

# modify tuples
try:
    if tuples[0] == "Computer":
        tuples[0] = "Laptop"
        print(tuples)
    else:
        tuples[0] = ""
        print(tuples)
except:
    print("Exception!!")

# how negative index works in python
numbers_tuple = ("one", "two", "ten", "five")
print(numbers_tuple[-1])
# to access a range of values we use slicing operator colon (:)
print("printing element 0 to -4: ", numbers_tuple[-4:-1])
# accessing unavailable index- value empty
print("printing empty tuple: ", numbers_tuple[:-4])
# printing all values using default [:]
print("printing all elements: ", numbers_tuple[:])

# delete specific tuple
try:
    if numbers_tuple: ["one"]
    del numbers_tuple[1]
    print(numbers_tuple)
except Exception as e:
    print(e)

# delete tuple
try:
    del numbers_tuple
    print(numbers_tuple)
except Exception as e:
    print(e)

# find the occurrence of the tuple elements, tuple count()
numbers_tuple = ("one", "two", "one", "four", "two")
print(numbers_tuple.count('one'))

# find index of specific elements of the tuple
print(numbers_tuple.index("two"))

# print elements by iterating through tuple elements
for elem in numbers_tuple:
    print(elem)

# try printing elements in the index that doesn't exist
products_ = ["TV", "LAPTOPS", "BATTERIES"]
print(products_[0])
try:
    print(products_[4])
except Exception as e:
    print(e)

# nested tuple
nested_tuple_ = ([1, 2, 3, 4], [9, 8, 7, 5])
print(nested_tuple_[1][1])
