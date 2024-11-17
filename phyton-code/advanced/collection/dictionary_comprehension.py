# Python code to demonstrate dictionary comprehension
# Lists to represent keys and values
keys = [1, 2, 3, 4, 5]
values = ['a', 'b', 'c', 'd', 'e']

# but this line shows dict comprehension here
myDict = {k: v for (k, v) in zip(keys, values)}

# We can use below too
# myDict = dict(zip(keys, values))
print(myDict)

# get the second-largest score
arr = {k: v for (k, v) in zip(keys, values)}
fir_lowest = min(arr)
sec_lowest = [i for i in arr if i > fir_lowest]

print(arr[fir_lowest])
print(arr[min(sec_lowest)])

