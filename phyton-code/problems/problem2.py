"""
String slicing in Python to Rotate a String

Given a string of size n, write functions to perform following operations on string.
Left (Or anticlockwise) rotate the given string by d elements (where d <= n).
Right (Or clockwise) rotate the given string by d elements (where d <= n).

Input : s = "RotateLeftAndRight"
        d = 2
Output : Left Rotation  : "tateLeftAndRightRo"
         Right Rotation : "htRotateLeftAndRi"
"""


# Function to rotate string left and right by d length

def rotate(input, d):
    # slice string in two parts for left and right
    Lfirst = input[0: d]
    Lsecond = input[d:]
    Rfirst = input[0: len(input) - d]
    Rsecond = input[len(input) - d:]

    # now concatenate two parts together
    print("Left Rotation : ", (Lsecond + Lfirst))
    print("Right Rotation : ", (Rsecond + Rfirst))


# Driver program
if __name__ == "__main__":
    input = 'RotateLeftAndRight'
    d = 2
    rotate(input, d)
