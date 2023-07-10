# 单例模式
# 开发模式: 单例模式

# class Student:
#     pass
#
#
# s = Student()
#
# s1 = Student()
# s2 = Student()
#
# print(s)
# print(s1)
# print(s2)

class Singleton:
    # 私有化  单例的地址就存在于__instance
    __instance = None
    name = "jacker"

    # 重写__new__
    def __new__(cls, *args, **kwargs):
        print("-------->__new__")
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
            return cls.__instance

        return cls.__instance

    def show(self, n):
        print("---------->show", Singleton.name, n)


s = Singleton()
s1 = Singleton()
s.show(5)
s1.show(7)


print(s)
print(s1)
