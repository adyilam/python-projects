"""
Finding the percentage
The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of
students. Print the average of the marks array for the student name provided, showing 2 places after the
decimal.

Example:
marks key: value pairs are
 2
alpha 20 30 40
beta 30 50 70
beta
The query_name is 'beta'. beta's average score (30+50+70)/3 is 50.0 .

Input Format
The first line contains the integer n, the number of students' records. The next n lines contain the names
and marks obtained by a student, each value separated by a space. The final line contains query_name,
the name of a student to query.

input:
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika

Explanation 0
Marks for Malika {52,56,60} are whose average  is (52+56+60) / 3 => 56.0

Output Format
Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.

output: 56.0
"""
# create a python dictionary
stud = {"name1": "1,2,3", "grade": "dict", "name3": "grade"}

# default looping gives keys
for keys in stud:
    print(keys)

# looping through keys
for keys in stud.keys():
    print(keys)

# looping through keys and value pair
for keys, values in stud.items():
    print(keys, values)

# Creating a dictionary of lists using list comprehension
dic = dict((val, range(int(val), int(val) + 2))
           for val in ['1', '2', '3'])

print(dic)



