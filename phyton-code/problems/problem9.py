"""
You are given a string and your task is to swap cases.
In other words, convert all lowercase letters to uppercase letters and vice versa.

For Example:
Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2

Function Description
Complete the swap_case function in the editor below.
swap_case has the following parameters:

string s: the string to modify
Returns
string: the modified string

Input Format
A single line containing a string .
Constraints: 1<len(s)<1000
"""

s = input("Enter any string less than 1000 characters: ")
chars = []


def swap_case(s):
    for c in s:
        if c.isupper():
            chars.append(c.lower())
        else:
            chars.append(c.upper())

    return ''.join(chars)  # convert array to string using join()


result = swap_case(s)
print(result)
