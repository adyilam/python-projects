# Generators are used to create iterators, but with a different approach.
# Generators are simple functions which return an iterable set of items, one at a time.
import random


def generate_numbers():
    # returns 6 numbers between 1 and 40
    for i in range(6):
        yield random.randint(1, 10)

    # returns a 7th number between 1 and 15
    yield random.randint(1, 5)


for random_number in generate_numbers():
    print("And the next number is... %d!" % (random_number))


