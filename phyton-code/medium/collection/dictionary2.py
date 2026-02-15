# 1. using defaultdict to add list in dict
from collections import defaultdict

lst = [(1, "Hello"), (2, 'there'), (1, 'folks')]
orDict = defaultdict(list)

# iterating over list of tuples
for key, val in lst:
    orDict[key].append(val)

print(orDict)

# 2. using json to add list in dict
# importing json
import json

# Initialisation of list
lst = [('ab', 1), ('cd', 2), ('ab', 3)]

# Initialisation of dictionary
dict = {}

# using json.dump()
hash = json.dumps(lst)

# creating a hash
dict[hash] = "converted"

# Printing dictionary
print(dict)

# create a python dictionary
stud = {"name1": "1,2,3", "grade": "dict", "name3": "grade"}

# default looping gives keys
for keys in stud:
    print(keys)

# looping through keys
for keys in stud.keys():
    print(keys)

# looping through keys and value pair
for keys, values in stud.items():
    print(keys, values)
# create a python dictionary
stud = {"name1": "1,2,3", "grade": "dict", "name3": "grade"}

# default looping gives keys
for keys in stud:
    print(keys)

# looping through keys
for keys in stud.keys():
    print(keys)

# looping through keys and value pair
for keys, values in stud.items():
    print(keys, values)

# Creating a dictionary of lists using list comprehension
dic = dict((val, range(int(val), int(val) + 2))
           for val in ['1', '2', '3'])

print(dic)

