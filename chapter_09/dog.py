# By convention, capitalized names refer to classes in Python
class Dog:
    """A simple attempt to model a dog."""

    # The function that's part of a class is a method
    # The _init_() method is a special method that Python runs automatically
    # when creating a new instance based on the class.
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        # the first parameter, self, is a reference to the instance itself
        # name and age, variables prefixed by self, are called attributes
        self.name = name
        self.age = age

    # sit and roll_over don't need additional info to run
    # defined to one parameter, self
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")

my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print(f"\nYour dog's name is {your_dog.nam}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()