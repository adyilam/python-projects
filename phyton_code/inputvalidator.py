min_len = 2
max_len = 20


# Name function
def validate_name_length(name, min_len, max_len):
    if len(name) < min_len:
        print("Name cannot be less than 2, Try again: ")
    elif len(name) > max_len:
        print("Name cannot be greater than 20, Try Again: ")
    return (len(name) >= min_len) and (len(name) <= max_len)


# Age function
def validate_age_length(age_int):
    if age_int < 5:
        print("Age cannot be less than 5, Try again: ")
    elif age_int > 89:
        print("Age cannot be greater than 89, Try Again: ")
        return (age_int >= 5) and (age_int <= 89)


while True:
    name = input("Enter Name:")
    try:
        print(validate_name_length(name, min_len, max_len))
        if validate_name_length(name, min_len, max_len):
            print("valid Name")
            break
        else:
            print("Invalid Name")
    except:
        print("Input mismatch error")
        break

while True:
    age = input("Enter Age:")
    age_int = int(age)  # cast to int
    try:
        if validate_age_length(age_int):
            print("valid Age")
            break
        else:
            print("Invalid Age")
    except:
        print("Input mismatch error")
        break


def hello_to_you(first_name, last_name):
    print(f"Hello, {first_name} {last_name}")


hello_to_you("Timmy", "Jones")  # Output:
# Hello,Timmy Jones
