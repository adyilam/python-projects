import functools
import time

#  filtering odd numbers
lst = filter(lambda x: x % 2 == 1, range(1, 20))
print(list(lst))

#  filtering odd square which are divisible by 5
lst = filter(lambda x: x % 5 == 0,
             [x ** 2 for x in range(1, 11) if x % 2 == 1])
print(list(lst))

#   filtering negative numbers
lst = filter((lambda x: x < 0), range(-5, 5))
print(list(lst))

#  implementing max() function, using functools.py
print(functools.reduce(lambda a, b: a if (a > b) else b, [7, 12, 45, 100, 15]))

# We can use the filter() function to perform custom slicing in a list
start_time = time.time_ns()
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_lst = list(filter(lambda x: x % 2 == 0, lst))
print(new_lst)
end_time = time.time_ns()
exec_time = end_time - start_time
print("Execution time: ", exec_time)

# using list comprehension
start_time = time.time_ns()
res = [val for val in lst if val % 2 == 0]
print(res)
end_time = time.time_ns()
exec_time = end_time - start_time
print("Execution time: ", exec_time)
