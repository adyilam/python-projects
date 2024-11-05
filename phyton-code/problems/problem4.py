"""
Given the participants' score_sheet for your University Sports Day, you are required to find the runner-up score.
You are given  scores. Store them in a list and find the score of the runner-up.

Input Format
The first line contains . The second line contains an array A[]  of n  integers each separated by a space.

"""

# find first max and second max of given array
arr = [2, 3, 7, 7, 8]
res = map(int, arr)
max1 = arr[0]
for i in range(len(arr)):
    if arr[i] > max1:
        max2 = max1
        max1 = arr[i]

print(max2)

# using map
arr = [2, 3, 6, 6, 5]
res = list(map(int, arr))
res.sort()
max1 = arr[0]
for i in range(len(res)):
    if res[i] > max1:
        temp = max1
        max1 = res[i]
        max2 = temp

print(max2)

# readable way using max() function
arr = [2, 3, 6, 6, 5]
res = list(map(int, arr))
res.sort()
max1 = max(res)
max2 = [i for i in res if i < max1]
print(max(max2))
