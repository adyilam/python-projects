# Lambda function

# function
def Greeting(str1, str2):
    return str1 + ' ' + str2


a = 'hello'
b = 'there'
c = Greeting(a, b)
print(c)

# using lambda function
a = "hello"
b = "there"
greeting = lambda str1, str2: str1 + ' ' + str2  # lambda
c = greeting(a, b)
print(c)

# Write a program using lambda functions to check
# if a number in the given list is odd. Print "True" if the number is odd or "False" if not for each element.
l = [2, 4, 7, 3, 14, 19]
for i in l:
    lambda_ = lambda x: (x % 2) == 0
    print(lambda_(i))
