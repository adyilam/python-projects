"""
How to filter an Object in python
Filtering an object in Python typically involves filtering its attributes or properties based on certain conditions.
Here’s an example using filter() and a lambda function to filter a list of objects based on an attribute:
"""


class Product:
    def __init__(self, name, qty):
        self.name = name
        self.qty = qty


# init Product object
products = [Product('Pen', 30), Product('pencil', 60), Product('TV', 500)]

# filter products its quantity more than 50
# using filter, lambada
filtered_products = list(filter(lambda prod: prod.qty >= 50, products))

# display result
for product in filtered_products:
    print(product.name, product.qty)
