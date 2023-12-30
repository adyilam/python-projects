# difference between list and tuple

# creating list and tuple
list_ = [1, 2, 3, 4]
tuple_ = [4, 5, 6, 7]
print(list_)
print(tuple_)

# list is mutable, can modify after initialization
# tuple is immutable, can't modify after initialization
list_ = ["list1", "list2", "list3"]
tuple_ = ("tuple1", "tuple2", "tuple3")

# modify list
list_[2] = "list2_modified"
print(list_)

# modify tuple
try:
    tuple_[2] = "tuple2_cannotmodified"
    print(tuple_)
except TypeError:
    print("Can't modify tuple")

# get the size of list or tuple
print("size of list: ", list_.__sizeof__())
print("size of tuple: ", tuple_.__sizeof__())
