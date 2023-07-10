# 在开发中看到一些私有化处理:  装饰器
class Student:
    def __init__(self, name, age):
        self.n = name  # 长度必须6位
        self.__a = age

    # 先有getxxx
    @property
    def age(self):
        return self.__a

    # 再有set, 因为set依赖get
    @age.setter
    def age(self, a):
        if a > 0 and a < 100:
            self.__a = a

    # def set_age(self, a):
    #     if a > 0 and a < 100:
    #         self.__a = a
    #     else:
    #         print("名字不是6位")
    #
    # def get_age(self, ):
    #     return self.__a

    def __str__(self):
        return f"姓名是:{self.n}, 年龄是{self.__a}"


s = Student("xie", 16)
s.name = "xiao_xie"
print(s.name)

s.age = 17

print(s.age)
print(s.__dir__)
# 私有化赋值
# s.set_age(30)
# print(s.get_age())
