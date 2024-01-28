products = ["Food", "Candy", "Shampoo", "Food"]
# iterating through the list, for loop
for x in products:
    print(x)

# using range
for i in range(len(products)):
    print(products)

# while loop
i = 0
while i < len(products):
    print(products[i])
    i = i + 1

# A shorthand for loop that will print all products in a list
[print(x) for x in products]

# python 'beak' - breaking a loop when a certain condition has meet
for i in range(len(products)):
    if products[i] == "Food":
        print("Match found: ")
        print(products)
        break
    else:
        continue


# Python 'pass' key: used in the loop. it is a placeholder for future change
def my_function(namelist):
    for j in range(len(namelist)):
        if namelist[j] == "":
            pass  # leaving an empty the block using pass key
        else:
            print("Name provided as " + namelist[j])  # the value at index 0 will not be displayed


names = ["", "Smith", "john"]
my_function(names)  # nothing will be displayed

# list build up, start a list as the empty list [], then use append() or extend() to add elements
list = []  # Start as the empty list
list.append('1')  # Use append() to add elements
list.append('4')
print(list)

# List Slices: work on lists just as with strings, and can also be used to change sub-parts of the list.
list_ = ['1', '2', '3', '4']
# print ['2', '3']
print(list_[1:-1])
# replace ['1', '2'] with ['5']
list_[0:2] = '5'
print(list_)
