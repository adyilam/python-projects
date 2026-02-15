"""
Task
Apply your knowledge of the .add() operation to help your friend Rupal.
Rupal has a huge collection of country stamps. She decided to count the
total number of distinct country stamps in her collection. She asked for your help.
You pick the stamps one by one from a stack of  country stamps.

Find the total number of distinct country stamps.
Input Format
    The first line contains an integer , the total number of country stamps.
    The next  lines contains the name of the country where the stamp is from.
Constraints
    0 < N < 1000
Output Format
    Output the total number of distinct country stamps on a single line.
Sample Input
    7
    UK
    China
    USA
    France
    New Zealand
    UK
    France
Sample Output
    5
"""

country = []


def get_distinct_country_stamp(N, countries):
    country_set = set()  # Initialize an empty set
    for country in countries:  # Iterate through the list of countries
        country_set.add(country)  # Add each country to the set
    return len(country_set)  # Return the number of distinct countries


# Input the number of countries
N = int(input().strip())

# Input the list of country stamps
countries = [input(f"Enter country {i + 1}: ").strip() for i in range(N)]
# countries = [input().strip()]

# Get the distinct count
count = get_distinct_country_stamp(N, countries)
print(f"count of distinct countries: {count}")
