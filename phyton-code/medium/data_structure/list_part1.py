# Lists are one of 4 built-in data types in Python used to store data_structure of data,
# List is a collection which is ordered and changeable. Allows duplicate members.
# the other 3 are Tuple, Set, and Dictionary

# Example
products = ["Food", "Candy", "Shampoo"]
print(products)
# print(products.index(0))

# list allow duplicates
products = ["Food", "Candy", "Shampoo", "Food", "Candy"]
print(products)
print(len(products))  # size of the list

# list can contain different data types , int , string..
products = ["22", "Candy", "Shampoo", "Food", "Candy"]
print(products)

# accessing products
print(products[0])
print(products[4])

# Negative index:
# Negative indexing means start from the end
print(products[-1])
print(products[-2])

# Range of Indexes:
# You can specify a range of indexes by specifying where to start and where to end the range.
# the return value will be a new list with the specified items.
products = ["Food", "Candy", "Shampoo", "Food", "Candy"]
print(products[1:4])
print(products[:4])
print(products[0:4])
print(products[2:])

# determine if a specific product is available
products = ["Food", "Candy", "Shampoo", "Food", "Candy"]
if "Shampoo" in products:
    print("True")
else:
    print("false")

# change the value of specific product in the list
products = ["Food", "Candy", "Shampoo", "Food", "Candy"]
if "Food" in products:
    index = products.index("Food")
    products[index] = "Ball"
    print(products)
else:
    print("product not available!")

# replace the product at index 1
products[1] = "Food"
print(products)

# replace the product at range of index 1 and 3 with value pen and pencil
products[1:3] = ["Pen", "Pencil"]
print(products)

# using append() method to add item at the end of the list
products.append("Water")
print(products)

# using insert() method to insert products in any specified list
products.insert(0, "Milk")
print(products)
products.insert(len(products)-1, "Yoghurt")
print(products)

# Extend() : To append elements from another list to the current list
products = ["Food", "Candy", "Shampoo", "Food", "Candy"]
clothes = ["Jeans", "Pants"]
products.extend(clothes)
print(products)

