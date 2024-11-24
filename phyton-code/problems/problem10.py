"""
Consider a list (list = []). You can perform the following commands:
    1.insert i e: Insert e integer  at i position .
    2.print: Print the list.
    3.remove e: Delete the first occurrence of integer e.
    4.append e: Insert integer e at the end of the list.
    5.sort: Sort the list.
    6.pop: Pop the last element from the list.
    7.reverse: Reverse the list.
"""

lis = [1, 2, 3]
N = int(input())

for i in lis:
    match i:
        case "insert":
            list.append(i)
        case "print":
            print(list)
        case "remove":
            # list[:-1] slicing
            del list[-1]  # del operator
        case "append":
            list.append(len(list), i)
        case "sort":
            list.sort()
        case "pop":
            list.pop()
        case "reverse":
            list.remove()