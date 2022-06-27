
class Employee:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def email(self):
        return f'{self.first_name}.{self.last_name}@email.com'

    @email.setter
    def email(self, name):
        self.first_name, self.last_name = name.split(' ')

    @email.deleter
    def email(self):
        print('Delete Email')
        self.last_name, self.first_name = None, None



employee = Employee('Sigurd', 'Sturlason')

print(employee.email)

employee.email = 'Snorry Svenson'

print(employee.email)

del employee.email