class A():
    pass

class B(A):
    pass

class C():
    pass


def fun():
    print(issubclass(B,A))
    print(issubclass(A,B))



