# is a  base class  父类  基类
# Exception
"""
继承:
    Student, Employee, Doctor -----> 都属于人类
    相同代码  ----->  代码冗余,  可读性不高

    将相同代码提取 ------> Person类
     Student, Employee, Doctor ------> 继承Person

        class Student(Person):
            pass
    特点:
        1. 如果类中不定义__init__, 调用父类 super class的__init__
        2. 如果类继承父类也需要定义自己的__init__, 就需要在当前类的__init__调用一下父类的__init__
        3. 如何调用父类__init__:
            super().__init__(参数u)
            super(类名, 对象).__init__(参数)
        4. 如果父类有eat(), 子类也定义一个eat方法, 默认搜索的原则: 先找当前类， 再去找父类
            s.eat()
            override:  重写(覆盖)
            父类提供的方法不能满足子类的需求, 就需要在子类中定义一个同名的方法, 而这种行为: 重写
        5. 子类的方法中也可以调用父类方法:
            super().方法名(参数)
"""


class Person:
    def __init__(self, name, age):
        self.n = name
        self.a = age

    def eat(self, *args):
        print(self.n + "正在吃饭")

    def run(self):
        print(self.n + "正在跑步")


class Student(Person):
    def __init__(self, name, age, class_room):
        # 如何调用父类的__init__
        super().__init__(name, age)  # super()  父类对象
        self.c = class_room

    def study(self, course):
        print(f"{self.n}正在学习{course}")

    def eat(self, food):
        super().eat()
        print(self.n + f"正在吃饭, 喜欢吃{food}")


class Employee(Person):
    def __init__(self, name, age, salary, manage):
        super().__init__(name, age)
        self.s = salary
        self.m = manage


class Doctor(Person):
    def __init__(self, name, age, patients):
        super(Doctor, self).__init__(name, age)
        self.p = patients


s = Student("xie", 18, 20)
s.run()
s.study("python")
s.eat("狮子头")

e = Employee("xie", 16, 1000, "big_xie")
e.run()
list1 = ["Yu", "Titer"]

d = Doctor("xie", 17, list1)
d.run()
