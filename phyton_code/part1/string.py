# modify string
s = "Change to upper case"
print(s.upper())

s = "CHANGE TO LOWER CASE"
print(s.lower())

# remove while space before or after a string
s = " remove white space "
print(s.strip())

# replace string
s = "Hello there"
print(s.replace("H", "Z"))

# split string
s = "key: value"
print(s.split(":"))

# concatenate string
x = "Hello"
y = "there"
print(x+y)
print(x + " " + y)

z = 10
# print(x + z)
print(y.format(z))

# convert to lower case
x = "HELLO"
print(x.casefold())
print("length of x " + str(len(x)))



