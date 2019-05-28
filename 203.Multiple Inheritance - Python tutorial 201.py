# 203.Multiple Inheritance - Python tutorial 201

class D:
    pass

class A(D):
    def class_a_method(self):
        return 'I\'m class A method'
    def hello(self):
        return 'hello fron class A'


class B(A,D):
    def class_b_method(self):
        return 'I\'m class B method'
    def hello(self):
        return 'hello fron class B'


class C(B,A,D):
    pass
instance_a = A()
instance_C = C()
print(instance_C.class_a_method())
print(instance_C.class_b_method())
print(instance_C.hello())
print(help(C))
print(C.mro())
print(C.__mro__)