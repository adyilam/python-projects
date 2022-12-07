products = ["Food", "Candy", "Shampoo", "Food"]
# iterating through the list, for loop
for x in products:
    print(x)

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
            pass      # leaving an empty the block using pass key
        else:
            print("Name provided as " + namelist[j])  # the value at index 0 will not be displayed


names = ["", "Smith", "john"]
my_function(names)     # nothing will be displayed
