"""
 check if a string can become empty by recursive deletion
 using String slicing
 Given a string “str” and another string “sub_str”. We are allowed
 to delete “sub_str” from “str” any number of times. It is also given that the “sub_str”
 appears only once at a time. The task is to find if “str” can become empty by removing “sub_str” again and again.
"""


def check_empty(input, pattern):
    # If both are empty
    if len(input) == 0 and len(pattern) == 0:
        return 'true'

    # If only pattern is empty
    if len(pattern) == 0:
        return 'false'

    while (len(input) != 0):

        # find sub-string in main string
        index = input.find(pattern)

        # check if sub-string founded or not
        if (index == (-1)):
            return 'false'

        # slice input string in two parts and concatenate
        input = input[0:index] + input[index + len(pattern):]
    return 'true'


# Driver program
if __name__ == "__main__":
    input = 'TESTESTEST'
    pattern = 'TEST'
    print(check_empty(input, pattern))
