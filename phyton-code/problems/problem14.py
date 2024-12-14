"""
Tuples: are data structures that look a lot like lists. Unlike lists, tuples are immutable (meaning that they cannot
be modified once created). This restricts their use because we cannot add, remove, or assign values;
however, it gives us an advantage in space and time complexities

Given an integer,n, and space-separated integers as input, create a tuple,t , of those n integers.
Then compute and print the result of hash(t).
Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.
Input Format
The first line contains an integer,n, denoting the number of elements in the tuple.
The second line contains space-separated integers describing the elements in tuple t.
Output Format
Print the result of hash(t).

Sample Input 0
2
1 2
Sample output
3713081631934410656
"""

# Example
a = 2
b = 3
a, b = b, a

print(f"{a} {b}")


# test tuples dynamic by accepting input from user
def solve(t):
    return hash(t)


n = int(input("Enter number of tuples ?"))
t = tuple(map(int, input().split()))
res = solve(t)
print(res)
