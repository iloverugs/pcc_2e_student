class User:
    """Describes and greets users"""

    def __init__(self, first_name, last_name, email, password):
        """Initialize first name, last name, email, and password attrbutes"""
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.login_attempts = 0

    def describe_user(self):
        """Describes the user"""
        print("User information:")
        print(f"\tName: {self.first_name} {self.last_name}")
        print(f"\tEmail: {self.email}")
        print(f"\tPassword: {self.password}")

    def greet_user(self):
        """Greets the user"""
        print(f"Hello {self.first_name}.")

    def increment_login_attempts(self):
        """Adds to login_attempts by 1 per attempt"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Resets login_attempts to 0"""
        self.login_attempts = 0

    def read_login_attempts(self):
        """Prints current number of login_attempts"""
        print(f"There have been {self.login_attempts} login attempts.")

# Instance of class, increase increment_login_attempts several times
peanut = User("Philip", "Legume", "peanutsrule@fkmail.com", "peanutsRb3st")

peanut.increment_login_attempts()
peanut.increment_login_attempts()
peanut.increment_login_attempts()
peanut.increment_login_attempts()
peanut.read_login_attempts()

peanut.reset_login_attempts()
peanut.read_login_attempts()

