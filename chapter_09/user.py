"""Class that represents users"""


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
