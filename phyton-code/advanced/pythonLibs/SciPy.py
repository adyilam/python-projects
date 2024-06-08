# source: w3school.com
# SciPy is a scientific computation library that uses NumPy underneath.
# SciPy stands for Scientific python
# It provides more utility functions for optimization, stats and signal processing.
# If SciPy uses NumPy underneath, why can we not just use NumPy?
# SciPy has optimized and added functions that are frequently used in NumPy and Data Science.
# The source code for SciPy is located at github repository https://github.com/scipy/scipy

# How many cubic meters are in one liter
from scipy import constants  # constants: Physical and mathematical constants and units.

print(constants.liter)

# speed of light in vacuum
print(constants.speed_of_light)

# electron mass
print(constants.electron_mass)

# Mass, how many kilogram is 1 gram
print(constants.gram)

# 1 grain in kilogram
print(constants.grain)
