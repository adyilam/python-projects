"""
The for loop with one or more inner for loops is called nested for loop
syntax:
for iterating_var in sequence:
   for iterating_var in sequence:
      statements(s)
   statements(s)
"""

# example1 - iterate over months and days
months = ["January", "February", "March"]
days = ["Monday", "Tuesday", "Wednesday"]

for i in months:
    for j in days:
        print(i + ":", j)

print('end of the line!')

# example2: while loop to find the prime numbers from 2 to 100 using while loop
i = 2
while (i < 25):
    j = 2
    while (j <= (i / j)):
        if not (i % j): break
        j = j + 1
    if (j > i / j): print(i, " is prime")
    i = i + 1
print("end of line!")
