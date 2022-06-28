class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = f"{first}.{last}@email.com"
        self.pay = pay

        Employee.num_of_emps += 1

    def full_name(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        """create a new instance parsing a string """
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

emp_1 = Employee('Karina', 'Schaffer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

Employee.set_raise_amt(1.05)

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

print('*' * 30)

emp_str_1 = 'Snorri-Sturlason-3000'
emp_str_2 = 'Gustav-Karlson-4000'

new_emp_1 = Employee.from_string(emp_str=emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)