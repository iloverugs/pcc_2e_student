#Make class Restaurant. __init__ stores 2 attributes
# restaurant_name and cuisine_type
# method called open_restuarant that prints a message restaurant is open

class Restaurant:
    """Describes a restaurant, name and cuisine type"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and cuisine type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Prints restaurant_name and cuisine_type"""
        print(f"{self.restaurant_name} serves {self.cuisine_type} food.")

    def open_restaurant(self):
        """Simulate the restaurant opening"""
        print(f"{self.restaurant_name} is now open.")

italian_restaurant = Restaurant("mario's spagetti", "italian")

italian_restaurant.describe_restaurant()
italian_restaurant.open_restaurant()