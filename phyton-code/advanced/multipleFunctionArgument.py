# It is possible to declare functions which receive a variable number of arguments,
# using the following syntax: def fun(first, second, third, *therest):
def function(first, second, third, *therest):
    print(first)
    print(therest)
result = function(1, 2, 3, 4, 5, 6)
print(result)
