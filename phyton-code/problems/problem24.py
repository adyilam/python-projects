"""
String validator
# Using any - Return True if bool(x) is True for any x in the iterable.
# If the iterable is empty, return False.
"""

s = input()

# Option1
is_alnum = False
is_alpha = False
is_digit = False
is_lower = False
is_upper = False

for c in s:
    if c.isalnum():
        is_alnum = True
    if c.isalpha():
        is_alpha = True
    if c.isdigit():
        is_digit = True
    if c.islower():
        is_lower = True
    if c.isupper():
        is_upper = True

print(is_alnum)
print(is_alpha)
print(is_digit)
print(is_lower)
print(is_upper)

# Option2
"""print(any(c.isalnum() for c in s))
print(any(c.isalpha() for c in s))
print(any(c.isdigit() for c in s))
print(any(c.islower() for c in s))
print(any(c.isupper() for c in s))
"""
