# iterating through the list
products = ["Food", "Candy", "Shampoo", "Food"]
for x in products:
    print(x)

# ---
for i in range(len(products)):
    print(products)

# while loop
products = ["Food", "Candy", "Shampoo", "Food"]
i = 0
while i < len(products):
    print(products[i])
    i = i + 1

# ----
# A shorthand for loop that will print all products in a list
products = ["Food", "Candy", "Shampoo", "Food"]
[print(x) for x in products]
