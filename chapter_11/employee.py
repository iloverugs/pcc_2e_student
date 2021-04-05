class Employee:
    """Gives a summary of an employee."""

    def __init__(self, firstname, lastname, yr_salary):
        """Initializes attributes describing employee."""
        self.firstname = firstname
        self.lastname = lastname
        self.yr_salary = yr_salary

    def give_raise(self, salary_raise=5000):
        """Adds amount to salary, default 5000."""
        self.yr_salary += salary_raise

    def get_employee_name(self):
        """Returns employee name."""
        employee_name = f"{self.firstname} {self.lastname}"
        return employee_name.title()

    def print_employee_information(self):
        print(f"Name: {Employee.get_employee_name(self).title()}\n" \
            f"Salary: {self.yr_salary}")