# String is data typ of python
# string is the collection of the characters
# surrounded by single quotes, double quotes, or triple quotes.

# creating string in python
# single quote
message = 'single quote string'
print(message)

# double quote
message = "double quote string"
print(message)

# triple quote
message = '''triple quote string'''
print(message)

# accessing string values with specific index
greeting = "Greetings"
print(greeting[0])
# print(greeting[9])  # throws out of range error, index 5 not exist

# accessing string value with index range
greeting = "Greetings"
print(greeting[0:5])
print(greeting[0:8])
print(greeting[0:9])  # Notice here : greeting[0]: G, but greeting[9] displays only greeting[8]:s

