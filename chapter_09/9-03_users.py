# Class named User. 2 attributes, first_name, last_name
# Additional attributes typically stored in a user profile
class User:
    """Describes and greets users"""

    def __init__(self, first_name, last_name, email, password):
        """Initialize first name, last name, email, and password attrbutes"""
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def describe_user(self):
        """Describes the user"""
        print("User information:")
        print(f"\tName: {self.first_name} {self.last_name}")
        print(f"\tEmail: {self.email}")
        print(f"\tPassword: {self.password}")

    def greet_user(self):
        """Greets the user"""
        print(f"Hello {self.first_name}.")

max118 = User("Max", "Power", "mp@fakeemail.com", "password123")
skk271 = User("Sarah", "Lin", "slin@fakeemail.com", "B3tt3rP@ssword")
peanut = User("Philip", "Legume", "peanutsrule@fkmail.com", "peanutsRb3st")

max118.describe_user()
skk271.describe_user()
peanut.describe_user()

max118.greet_user()
skk271.greet_user()
peanut.greet_user()