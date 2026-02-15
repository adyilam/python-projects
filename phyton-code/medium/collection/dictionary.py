# Dictionary is a data structure used to store data.
# The data is stored as key-value pairs using a Python dictionary.
# It is mutable.
# Keys must only have one component.
# Values can be of any type, including integer, list, and tuple.
# A dictionary is, in other words, a group of key-value pairs,
# where the values can be any Python object.
# The keys, in contrast, are immutable Python objects, such as strings, tuples, or numbers.

# crate empty dictionary
dict_ = {}
print("Empty dictionary: ", dict_)

# creating dictionary
d = {"Name": "laptop", "accessories": "charger", "description": "electronics"}  # syntax
print("Electronics in dictionary: ", d)

# get the length of dict
print("length of dict:   ", len(dict))

# create dictionary using dict()
# dict1_ = dict([{"Name": "laptop", "accessories": "charger", "description": "electronics"}])   # dict object not callable
# print("create dictionary using dict(): ", dict1_)

# accessing values of dictionary using key (it's unique)
print("Name: ", dict["Name"])
print("Name: ", dict.get("Name"))
print("Name: ", dict["accessories"])
print("Name: ", dict["description"])

# get dictionary element using key
del dict["Name"]
print(dict)

# get the keys of dict element using key() method
print("KEYS OF dict: ", dict.keys())

# delete dictionary element using pop()
pop_key = dict.pop("accessories")
print(dict)

# iterating dictionary to print the keys
student = {"name": "john smith", "age": 20, "gender": "Male"}
print(">>>>>>>>>>>>>> keys: ")
for i in student:
    print(i)

# iterating dictionary to print the values
print(">>>>>>>>>>>>>> values: ")
for i in student:
    print(student[i])

# iterating dictionary to print the values() method
print(">>>>>>>>>>>>>> print values using values(): ")
for i in student.values():
    print(i)

# iterating dictionary to print the items() method
print(">>>>>>>>>>>>>> print key,value: ")
for i, j in student.items():
    print(i, j)

# iterating dictionary to print the key and value, using items()
for i, j in student.items():
    print(i)

# creating dict object range
range_ = {"start": 0, "end": 10}
for i in range(0, 5):
    print(i)

# shallow copy the element of dict using copy()
prod = {1: 'book', 2: 'pen', 3: 'cloth'}
prod_copy = prod.copy()
print(prod_copy)

# delete element using pop()
delete_first_elm = prod_copy.pop(1)
print(prod_copy)

# accessing values in specified keys
print("value at index 3: ", prod.get(3))

# update values in specified keys
prod.update({3: "SPORT ITEM"})
print("updated value at index 3: ", prod.get(3))

# removes the most recent key-value pair entered using popitem() method
prod_copy.popitem()
print(prod_copy)

# clear() build in dictionary method
prod.clear()
print(prod)
