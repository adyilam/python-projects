"""
python do not have switch case until python version 3.9, the later version supports switch case.
Structural Pattern Matching (Python 3.10 and above)
"""


# 1. handling case using if-else
def get_day_type(day):
    if day == "Saturday" or day == "Sunday":
        return "Weekend"
    elif day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
        return "Weekday"
    else:
        return "Invalid day"


print(get_day_type("Monday"))
print(get_day_type("Saturday"))
print(get_day_type("Invalid"))


# 2. handling the case using dictionary
def get_day_type(day):
    day_types = {
        "Monday": "Weekday",
        "Tuesday": "Weekday",
        "Wednesday": "Weekday",
        "Thursday": "Weekday",
        "Friday": "Weekday",
        "Saturday": "Weekend",
        "Sunday": "Weekend"
    }
    return day_types.get(day, "Invalid day")


print(get_day_type("Monday"))
print(get_day_type("Saturday"))
print(get_day_type("Invalid"))


# 3. handling case using Structural Pattern Matching (Python 3.10 and above)
def get_day_type(day):
    match day:
        case "Saturday" | "Sunday":
            return "Weekend"
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return "Weekday"
        case _:
            return "Invalid day"


print(get_day_type("Monday"))
print(get_day_type("Saturday"))
print(get_day_type("Invalid"))
