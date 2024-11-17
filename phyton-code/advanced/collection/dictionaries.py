# Dictionaries: A dictionary is a data type similar to arrays, but works with
# keys and values instead of indexes. Each value stored in a dictionary can be accessed using a key,
# which is any type of object (a string, a number, a list, etc.) instead of using its index to address it.

# set list of phone numbers
phonebook = {"Tom": 123456789, "Ali": 3344245645, "Rahel": 5565768898}
print(phonebook)

# retrieve each phone number from the phone book list
for name, phone in phonebook.items():
    print(name, phone)

print("==========================")
# delete specific phone number using pop or del
del phonebook["Ali"]
print(phonebook)

# remove phone list using pop
phonebook.pop("Tom")
print(phonebook)

# check if name exist remove from phonebook
if "Ali" in phonebook:
    del phonebook["Ali"]
else:
    print("Contact is not in the phone book list")


