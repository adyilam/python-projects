"""
If we want to add a single element to an existing set,
we can use the .add() operation.
It adds the element to the set and returns 'None'.
"""
# Example
s = set('HelloThere')
s.add('H')
print(s)  # {'r', 'H', 'l', 'h', 'o', 'e', 'T'}
print(s.add('HelloThere'))  # None
print(s)  # {'r', 'H', 'l', 'h', 'o', 'HelloThere', 'e', 'T'}
