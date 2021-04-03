# Start with class form 9-01, Create 3 different instances from the class
# Call describe_restaurant() for each instance

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

korean_restaurant = Restaurant('Nomu Mashiso!', 'korean')
breakfast_restaurant = Restaurant('Maple Syrup and Bacon', 'breakfast')
japanese_restaurant = Restaurant('Arigato', 'japanese')

korean_restaurant.describe_restaurant()
breakfast_restaurant.describe_restaurant()
japanese_restaurant.describe_restaurant()