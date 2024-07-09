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

# Optimizing Functions: all the algorithms in
# Machine Learning are nothing more than a complex equation
# that needs to be minimized with the help of given data.
from scipy.optimize import root
from math import cos


def eqn(x):
    return x + cos(x)


myroot = root(eqn, 0)
print(myroot.x)

# Minimize the function
# Minimize the function x^2 + x + 2 with BFGS
from scipy.optimize import minimize


def eqn(x):
    return x ** 2 + x + 2


mymin = minimize(eqn, 0, method='BFGS')

print(mymin)

