
class Employee:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def _email(self):
        return f'{self.first_name}.{self.last_name}@email.com'

    @_email.setter
    def _email(self, name):
        self.first_name, self.last_name = name.split(' ')

    @_email.deleter
    def e_mail(self):
        print('Delete Email')
        self.last_name, self.first_name = None, None

karl = Employee('Karl', 'Gustav')
karl._email = "Wilhelm Ogrange"
print(karl._email)