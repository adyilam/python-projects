import numpy as np

# from a python list
a = np.array([1, 2, 3, 4])
print(a)

# using special function
b = np.zeros((2, 3))  # create an array of zeros
print(b)
c = np.ones((3, 2))  # create an array of ones
print(c)
d = np.random.rand(2, 2)  # create an array random value
print(d)

# array indexing and slicing
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(a[1, 2])
print(a[:, 1])
print(a[1:, :2])

# Array operations
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# addition
c = a + b
print(c)

# Multiplication
d = a * b
print(d)

# Sum of all elements in array a
e = np.sum(a)
print(e)

# Array reshaping
a = np.array([1, 2, 3, 4, 5, 6])
# reshape array in to 2x3 array
b = a.reshape(2, 3)
print(b)

# Array concatenation
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
# concatenate along rows
c = np.concatenate((a, b), axis=0)
print(c)

# concatenate along cols
c = np.concatenate((a, b), axis=1)
print(c)

# Conditions and boolean array
a = np.array([1, 2, 3, 4, 5])
condition = a > 2
print(condition)

# filter element based on the value of the condition
b = a[condition]
print(b)

# Mathematical functions
a = np.array([1, 2, 3, 4, 5])
# sin of a
b = np.sin(a)
print(b)
# exponent of a
c = np.exp(a)
print(c)
# square root of a
d = np.sqrt(a)
print(d)

# Loading and Saving arrays
# Save an array to a binary file
a = np.array([1, 2, 3, 4, 5])
np.save('data.npy', a)

# Load an array from a binary file
b = np.load('data.npy')

# Array statistics
a = np.array([1, 2, 3, 4, 5])
# get mean of array a
mean_value = np.mean(a)
print(mean_value)
# get median of array a
median_value = np.median(a)
print(median_value)
# get dtd
std_dev = np.std(a)
print(std_dev)

# Random sampling, generate random numbers and perform random sampling from array
# generate 5 random numbers between 0 and 1
random_nums = np.random.rand(5)
print(random_nums)
# randomly select 3 elements from an array
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
random_elements = np.random.choice(a, size=3, replace=False)
print(random_elements)

# Array sorting
a = np.array([1, 4, 2, 5, 3])
sorted_a = np.sort(a)
print(sorted_a)
# sort a 2d array along with column
b = np.array([[4, 1, 2], [7, 6, 5]])
sorted_b = np.sort(b, axis=1)
print(sorted_b)

# Array manipulation with numpy
a = np.array([1, 2, 3, 4, 5, 6])
# reverse the order of the array element
reversed_a = np.flip(a)
print(reversed_a)
# repeat elements of the array
repeated_a = np.repeat(a, 2)
print(repeated_a)

# Array comparisons
a = np.array([1, 2, 3, 4, 5])
b = np.array([3, 4, 5, 6, 7])

# element-wise comparison
greater_than = a > b
print(greater_than)
less_than_equal = a <= b
print(less_than_equal)
