"""A set of classes used to represent admin and admin privileges"""
from user import User

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
