# Given records
# records = [["chi", 20.0], ["beta", 50.0], ["alpha", 50.0]]
# records = [["Harry", 37.21], ["Berry", 37.21], ["Tina", 37.2], ["Akriti", 41], ["Harsh", 39]]

records = [[4, "Rachel"], [-50, "Mawer"], [-50, "Sheen"], [-50, "Shaheen"], [51, ""]]

# Extract valid records with numeric grades
valid_records = [(name, float(grade)) for name, grade in records if
                 isinstance(grade, (int, float, str)) and str(grade).replace('.', '', 1).isdigit()]

# Extract unique grades and sort them
unique_grades = sorted({grade for _, grade in valid_records})

# Find the second-lowest grade
second_lowest_grade = unique_grades[1] if len(unique_grades) > 1 else None

# Collect names of students with the second-lowest grade
if second_lowest_grade is not None:
    second_lowest_names = sorted(name for name, grade in valid_records if grade == second_lowest_grade)
else:
    second_lowest_names = []

# Print the names, one per line
for name in second_lowest_names:
    print(name)

"""
second_lowest_grade = unique_grades[1] if len(unique_grades) > 1 else None
        print(second_lowest_grade)

        if second_lowest_grade is not None:
            second_lowest_names = sorted(name for name, grade in valid_records if grade == second_lowest_grade)
        else:
            second_lowest_names = []

        for name in second_lowest_names:
            print(name)
"""
