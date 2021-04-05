import unittest
from employee import Employee

class TestEmployeeClass(unittest.TestCase):
    """Test for the class Employee."""

    def setUp(self):
        """
        Create values for each attribute for use in all test methods.
        """
        self.employeetest = Employee('bryan', 'merges', 50_000)
        self.salary_test = [5000, 6000]

    def test_employee_default_raise(self):
        """Test that employee with default raised salary has been calculated."""
        self.employeetest.give_raise()
        self.assertEqual(
            self.salary_test[0]+50000, self.employeetest.yr_salary)

    def test_employee_add_raise(self):
        """Test that employee with new raised salary has been calculated"""
        self.employeetest.give_raise(self.salary_test[1])
        self.assertEqual(
            self.salary_test[1]+50000, self.employeetest.yr_salary)

if __name__ == '__main__':
    unittest.main()