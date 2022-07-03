class PrintOnCreation(type):

    def __call__(self, *args, **kwargs):
        print("The instance of class is created!")
        print(*args, **kwargs)

class NullInstance(type):

    def __call__(cls, *args, **kwargs):
        print(*args, **kwargs)
        raise TypeError("No instance created")

class EnforcerMeta(type):

    def __new__(cls, clsname, bases, clsdict):
        for name in clsdict:
            if name.lower() != name:
                print(f"Inappropriate method name: {name}")
        return super().__new__(cls, clsname, bases, clsdict)


class Geometry(metaclass=PrintOnCreation):

    def __init__(self, name):
        self.name = name

class Root(metaclass=EnforcerMeta):
    pass

class ChildA(Root):
    def method_name(self):
        pass

class ChildB(Root):
    def methodName(self):
        pass

if __name__ == '__main__':
    g = Geometry(None)

    a = ChildA()
    b = ChildB()