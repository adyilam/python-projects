"""
Given the names and grades for each student in a class of  students,
store them in a nested list and
print the name(s) of any student(s) having the second_lowest grade.
Note: If there are multiple students with the second_lowest grade,
order their names alphabetically and print each name on a new line.
"""

python_students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
python_students.sort()
# index: 0,1,2
# value of the first dict, python_students[0][1] = 37.21

students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

# Extract all scores
scores = [student[1] for student in students]

# Find the minimum and second minimum scores
first_min_score = min(scores)
second_min_score = min(score for score in scores if score > first_min_score)

# Find students with the first minimum score
first_min_students = [student[0] for student in students if student[1] == first_min_score]

# Find students with the second minimum score
second_min_students = [student[0] for student in students if student[1] == second_min_score]


# Output the results
print("Student(s) with the lowest score:", first_min_students)
print("Student(s) with the second lowest score:", second_min_students)
