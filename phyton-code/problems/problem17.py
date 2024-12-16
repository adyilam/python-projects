"""
Consider a list (list = []). You can perform the following commands:
1. insert i e: Insert integer e at position i.
2. print: Print the list.
3. remove e: Delete the first occurrence of integer e.
4. append e: Insert integer e at the end of the list.
5. sort: Sort the list.
6. pop: Pop the last element from the list.
7. reverse: Reverse the list.
Initialize your list and read in the value of n followed by n lines of commands where each command will be of the 7 types
listed above. Iterate through each command in order and perform the corresponding operation on your list.

"""

# Solution for the above problem
mylist = []
N = int(input().strip())

for _ in range(N):
    cmd = input().strip().split()

    if cmd[0] == "insert":
        mylist.insert(int(cmd[1]), int(cmd[2]))
    elif cmd[0] == "print":
        print(mylist)
    elif cmd[0] == "remove":
        mylist.remove(int(cmd[1]))
    elif cmd[0] == "append":
        mylist.append(int(cmd[1]))
    elif cmd[0] == "sort":
        mylist.sort()
    elif cmd[0] == "pop":
        mylist.pop()
    elif cmd[0] == "reverse":
        mylist.reverse()
    else:
        print(f"Invalid command: {cmd[0]}")
