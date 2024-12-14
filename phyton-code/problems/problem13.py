"""
You are asked to ensure that the first and last names of people begin with a capital letter in their passports.
For example, alison heck should be capitalised correctly as Alison Heck.

alison heck   => Alison Heck
Given a full name, your task is to capitalise the name appropriately.

Input Format
A single line of input containing the full name,S.

Constraints
    0< LEN(S) < 1000
    The string consists of alphanumeric characters and spaces
Note: in a word only the first character is capitalised. Example 12abc when capitalised remains 12abc.

Output Format
Print the capitalised string,S.
Sample Input
    alen chris
Sample output
    Alen Chris
"""

# Option 1
print("\n Option 1: ")


def capitalize_string(str):
    for i in range(len(str)):
        print(str[i].capitalize(), end=" ")


name = "hello world"
capitalized_name = name.split()
capitalize_string(capitalized_name)

# Option 2
print("\n Option 2: ")


def solve(s):
    output = []
    name = s.split(" ")

    for i in range(len(name)):
        output.append(name[i].capitalize())

    return " ".join(output).strip()


s = " hello  world  lol  "
res = solve(s)
print(res)
