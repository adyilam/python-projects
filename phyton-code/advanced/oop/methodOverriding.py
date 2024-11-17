"""
Method overriding occurs when a child class provides a specific implementation for a method
that is already defined in its parent class. The implementation in
the child class replaces the one in the parent class when the method is called on an instance of the child class.
"""


# In this example, the Dog and Cat class overrides the speak method of the Animal class.
class Animal:
    def speak(self):
        return "Make sound"


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


# Creating an instance of the Dog class
dog = Dog()
print(dog.speak())  # Output: Woof!

cat = Cat()
print(cat.speak())  # Output: Meow!
