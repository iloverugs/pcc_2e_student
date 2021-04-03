class Restaurant:
    """Describes a restaurant, name and cuisine type"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name, cuisine type, number served"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Prints restaurant_name and cuisine_type"""
        print(f"{self.restaurant_name} serves {self.cuisine_type} food.")

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

new_restaurant = Restaurant('YumYum', 'gummy bears')
new_restaurant.read_number_served()

# new_restaurant.number_served = 11
# new_restaurant.set_number_served(12)
new_restaurant.increment_number_served(16)
new_restaurant.read_number_served()

new_restaurant.increment_number_served(23)
new_restaurant.read_number_served()