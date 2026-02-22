"""
An Abstract Base Class (ABC) is used to achieve data abstraction by defining a common interface for its subclasses.
    It cannot be instantiated directly and serves as a blueprint for other classes

Abstract classes are created using abc module and @abstractmethod decorator, allowing developers
    to enforce method implementation in subclasses while hiding complex internal logic.
"""
from abc import abstractmethod, ABC


class Car(ABC):  # Inherit from ABC
    @abstractmethod
    def makes(self):
        # Abstract methods can have an implementation in the base class,
        # but must still be overridden in subclasses.
        pass


class BMW(Car):
    def makes(self):
        return "BMW Group"


class Toyota(Car):
    def makes(self):
        return "Toyota"


# TypeError: Can't instantiate abstract class Car without an implementation for abstract method 'makes'
# Car = Car()

# This works fine:
bmw = BMW()
print(bmw.makes())

# This works fine:
toyota = Toyota()
print(toyota.makes())
