# Python Object-Oriented Programming

# Instance -- self -- is passed automatically.
class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

# Calling method on class
print(Employee.fullname(emp_1))

# Calling method on instance
print(emp_1.fullname())
