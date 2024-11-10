"""
Advantages of using recursion

A complicated function can be split down into smaller sub-problems utilizing recursion.
Sequence creation is simpler through recursion than utilizing any nested iteration.
Recursive functions render the code look simple and effective.
Disadvantages of using recursion

A lot of memory and time is taken through recursive calls which makes it expensive for use.
Recursive functions are challenging to debug.
The reasoning behind recursion can sometimes be tough to think through.
"""
import math


# Fibonacci sequence is the integer sequence of 0, 1, 1, 2, 3, 5...
# Program to print the fibonacci series upto n_terms

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


num = 8
print("fibonacci of n: ")
for i in range(num):
    print(fibonacci(i))


# What is Factorial Recursion in Python?
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


print("factorial of ", num, ": ", factorial(num))

# using python math.math.factorial() function
print("factorial of ", num, ": ", math.factorial(num))
