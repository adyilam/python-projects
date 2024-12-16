"""
Exception Handling
Task
    You are given two values a and b.
    Perform integer division and print a/b.
    Input Format
    The first line contains T, the number of test cases.
    The next T lines each contain the space separated values of a and b.
Constraints
    0 < T < 10
Output Format
    Print the value of a/b.
    In the case of ZeroDivisionError or ValueError, print the error code.

Sample Input
    3
    1 0
    2 $
    3 1
Sample Output
    Error Code: integer division or modulo by zero
    Error Code: invalid literal for int() with base 10: '$'
    3
"""

T = int(input().strip())
for i in range(T):
    try:
        a, b = input().strip().split()
        result = int(int(a) / int(b))
    except ZeroDivisionError as e:
        print(f"Error Code: integer division or modulo by zero")
    except ValueError as ve:
        print(f"Error Code: {ve}")
    else:
        print(result)
