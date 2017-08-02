"""
Basic examples of Using classes in python
"""


class Employee:
    """
    This is an employee class
    """
    # These are class variables
    emp_count = 0
    company_name = 'Test'

    # this is special method for class constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_count(self):
        return Employee.emp_count

    def display_employee(self):
        return self.name, self.age


if __name__ == '__main__':
    employee = Employee('santosh', 26)
    print(__name__)
    print(Employee.__name__)
    print(Employee.__module__)

    print(employee.name)
    print(employee.age)

    print(Employee.__doc__)
    print(Employee.__bases__)
    print(Employee.__dict__)
