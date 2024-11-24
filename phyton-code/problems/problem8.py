"""
Given an integer,n, perform the following conditional actions:
If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20, print Not Weird

Input Format
A single line containing a positive integer,n.
Constraints 1<=n<=100
Output Format
Print Weird if the number is weird. Otherwise, print Not Weird.

"""
n = int(input("Enter any number between 1 to 100: "))
if n % 2 != 0:
    print("Weird")
# If n is even and in the inclusive range of 2 to 5, print Not Weird
elif (n % 2 == 0) & (n in range(2, 7)):
    print("Not Weird")
# If n is even and in the inclusive range of 6 to 20, print Weird
elif (n % 2 == 0) & (n in range(6, 21)):
    print("Weird")
# If n is even and greater than 20, print Not Weird
elif (n % 2 == 0) & (n > 20):
    print("Not Weird")
