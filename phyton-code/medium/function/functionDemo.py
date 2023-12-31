# python function syntax
# def function_name(parameters):
"""the block of code goes below"""


# code block

# calling a function
def greetings(string):
    return string


print("Greetings : ", greetings("hello there!!"))


# user-defined function
def area_circle(radius):
    return 3.14 * radius ** 2


def area_rectangle(length, width):
    return length * width


# call different functions
area_of_a_circle_ = area_circle(2)
area_of_a_rectangle_ = area_rectangle(2, 3)
print("The area of a circle is: ", area_of_a_circle_)
print("The area of a rectangle is: ", area_of_a_rectangle_)


# handling exception
def add(num1, num2):
    return num1 * num2


print("passing one argument to add() function ")
try:
    add(2)
except:
    print("Error: function takes two argument!!")


# variable length arguments
# "args" and "kwargs" refer to arguments not based on keywords.
def employees_name(*args_list):
    name = []
    for i in args_list:
        name.append(i.upper())
        return name


print("Employees list: ")
employee_names = employees_name('Alex smith', 'Marta ben', 'Tom cruise')
print(employee_names)


# defining a function
def employees(**kwargs_list):
    name = []
    for key, value in kwargs_list.items():
        name.append([key, value])
        return name


print("Employees list: ")
# Passing kwargs arguments
names = employees(One="Alex smith", Two="Marta ben", Three="Tom cruise")
print(names)
