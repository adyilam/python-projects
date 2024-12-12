"""
Given an integer, n, print the following values for each integer i  from 1 to n:
    1. Decimal
    2. Octal
    3. Hexadecimal (capitalized)
    4. Binary

"""

# Convert decimal to another
number = 10
# Convert to decimal
binary = "{0:b}".format(number)
print(binary)

# Convert to octal
octal = "{0:o}".format(number)
print(number)

# Convert to hexadecimal
hexadecimal = "{0:x}".format(number)
print(number)


def convert_to_decimal(decimal):
    for i in range(1, decimal + 1):
        width = len(bin(decimal)[2:])

        # Option 1
        print(f"{i}".rjust(width),
              "{0:o}".format(i).rjust(width),
              "{0:X}".format(i).rjust(width),
              "{0:b}".format(i).rjust(width))

        """
        # Option 2
        print(f"{i:{width}d} "
              f"{i:{width}o} "
              f"{i:{width}X} "
              f"{i:{width}b}")
        """


n = int(input("Enter any integer: "))
convert_to_decimal(n)
