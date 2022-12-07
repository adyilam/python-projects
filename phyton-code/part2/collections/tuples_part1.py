# A collection of ordered and immutable objects is known as a tuple.
# Tuples and lists are similar as they both are sequences.
# Tuples can not modify, but we can modify list after created
# When we create Tuples used parenthesis, List used square brackets

# how to crate tuple in different types and forms
activity_tuple_string = ("Music", "Movie", "Sport")
int_tuple = (10, 20, 30)
activity_tuple_string_no_parenthesis = "Music", "Movie", "Sport"
empty_tuple = ()
print(activity_tuple_string, int_tuple, activity_tuple_string_no_parenthesis, empty_tuple)

tuples = "Computer", "Water", 55, 10, ["Food", "Books"]
print(tuples)

# modify tuples
try:
    if tuples[0] == "Computer":
        tuples[0] = "Laptop"
        print(tuples)
    else:
        tuples[0] = ""
        print(tuples)
except:
    print("Exception!!")


