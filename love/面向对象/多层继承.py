# class Person:
#     def __init__(self, name):
#         self.n = name
#
#     def eat(self):
#         print("-----------eat_1")
#
#     def eat(self, food):
#         print("--------------eat", food)
#
#
# p = Person("jacker")
# p.eat("汉堡包")
class Base:
    def test(self):
        print("--------Base")


class A(Base):
    def test(self):
        print("----------AAAAAA")


class B(Base):
    def test(self):
        print("----------BBBBBB")


class C(Base):
    def test(self):
        print("-----------CCCCCC")


class D(A, B, C):
    pass


d = D()
d.test()
import inspect

print(inspect.getmro(D))
print(D.__mro__)
c = C()
c.test()


"""
Python 允许多继承
def 子类(父类1, 父类2,.....):
    Pass

如果父类中有相同名称方法, 搜索顺序

"""