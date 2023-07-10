# 多继承的搜索顺序:  经典类  新式类
class P1:
    def foo(self):
        print("p1---->foo")

    def bar(self):
        print("p1---->bar")


class P2:
    def foo(self):
        print("p2---->foo")


class C1(P1, P2):
    pass


class C2(P1, P2):
    def bar(self):
        print("C2---->bar")


class D(C1, C2):
    pass


d = D()
d.foo()
d.bar()
print(D.__mro__)

# Python 2

