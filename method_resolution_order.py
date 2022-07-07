class Root(object):
    def f(self):
        print("Root.f", self)

class A(Root):
    def f(self):
        print("A.f", self)
        super().f()

class B(Root):
    def f(self):
        print("B.f", self)
        super().f()

class C(A, B): # mro( C, A, B, Root, object)
    def f(self):
        print("C.f", self)
        super().f()


# class D(A, C):  error because C inherit from A


if __name__ == '__main__':

    print([cls.__name__ for cls in C.__mro__])

    c = C()
    c.f()