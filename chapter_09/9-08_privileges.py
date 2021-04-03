"""A set of classes used to represent users and admin privileges"""

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


class Privileges:
    """Describes administrator privileges"""

    def __init__(
        self, privileges = [
                "can add post", "can delete post",
                "can ban user", "can lockdown thread"
                ]
            ):
        """Initialize the admin's privileges"""
        self.privileges = privileges

    def show_privileges(self):
        """Prints administrator's set of privileges"""
        print("The administrator has the listed set of privileges:")
        for privilege in self.privileges:
            print(f"\t{privilege}")


class Admin(User):
    """Describes a user with special privileges"""

    def __init__(self, first_name, last_name, email, password):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an Administrator.
        """
        super().__init__(first_name, last_name, email, password)
        self.admin_privileges = Privileges()


User_Clark = Admin('Clark', 'Dalpee', 'cdalphee@fakeemail.com', '9skie8@e8dS')
User_Clark.greet_user()
User_Clark.admin_privileges.show_privileges()