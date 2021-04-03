"""A class used to represent restaurants"""

class Restaurant:
    """Represents aspects of a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name, cuisine type, number served"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Prints restaurant_name and cuisine_type"""
        print(f"{self.restaurant_name} serves {self.cuisine_type}.")

    def open_restaurant(self):
        """Simulate the restaurant opening"""
        print(f"{self.restaurant_name} is now open.")

    def read_number_served(self):
        """Prints number served at restaurant"""
        print(f"There have been {self.number_served} guests served.")

    def set_number_served(self, past_customers):
        """
        Sets number_served to new value
        Reject Value if less than previous value
        """
        if past_customers >= self.number_served:
            self.number_served = past_customers
        else:
            print("It's impossible to have less customers than before!")

    def increment_number_served(self, new_customer):
        """Add given amount to the number_served value"""
        if new_customer >= 1:
            self.number_served += new_customer

class IceCreamStand(Restaurant):
    """Represents aspects of restaurant, specific to ice cream stands."""

    def __init__(self, restaurant_name, cuisine_type):
        """
        Initialize attributes of parent class.
        Then initialize attributes specific to IceCreamStand.
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['chocolate', 'vanilla', 'pistachio', 'strawberry']

    def list_flavors(self):
        """Print a list of all flavors."""
        print("This stand has the following ice cream flavors: ")
        for flavor in self.flavors:
            print(f"\t{flavor}")