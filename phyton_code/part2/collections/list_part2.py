# to remove product in the products list use
products = ["Food", "Candy", "Shampoo", "Food", "Candy"]
products.remove("Candy")  # only the first item Candy removed
print(products)

# use pop() to remove specified index
products.pop(0)
print(products)

# remove the last product in the list
products = ["Food", "Candy", "Shampoo", "Food"]
products.pop()
print(products)

# del key work can remove the whole list or remove specific product in the list
products = ["Food", "Candy", "Shampoo", "Food"]
del products[1]
print(products)

# delete the ist
del products
# print(products)   # throws exception : NameError: name 'products' is not defined

# clear() method clears the value of the list
products = ["Food", "Candy", "Shampoo", "Food"]
products.clear()
print(products)

