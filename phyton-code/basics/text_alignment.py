"""
Text Alignment
In Python, a string of text can be aligned left, right and center.
"""
# ljust(width) , This method returns a left aligned string of length width.
width = 20
print('Text Alignment'.ljust(width, '-'))

# .center(width) , This method returns a centered string of length width.
width = 20
print('Text Alignment'.center(width, '-'))

# .rjust(width), This method returns a right aligned string of length width.
width = 20
print('HackerRank'.rjust(width, '-'))
