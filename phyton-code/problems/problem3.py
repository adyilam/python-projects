"""
You are given three integers x, y and z representing the dimensions of a cuboid along with an integer n .
Print a list of all possible coordinates given by (i,j,k)  on a 3D grid where the sum of i+j+k is not equal to n.
Here, 0 <=i<=x, O<=j<=y,0<=k<=z. Please use list comprehensions rather than multiple loops,
Example:
    input:
    1
    1
    1
    2
    output:
    [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

    Expected:
    [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
    Actual:
    [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]

"""
n = 2
x = 1
y = 1
z = 1

# readable way
print([[i, j, k] for i in range(0, x + 1) for j in range(0, y + 1) for k in range(0, z + 1) if (i + j + k) != n])

# equivalent loop
res = []
for i in range(0, x + 1):
    for j in range(0, y + 1):
        for k in range(0, z + 1):
            if (i + j + z) != n:
                res.append([i, j, k])
                print(res)
