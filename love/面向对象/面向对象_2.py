# 定义类和属性
class Student:
    # 类属性
    name = "xie"
    age = 16


xie = Student()
# print(xie.gender)  # AttributeError: 'Student' object has no attribute 'gender'

xie.age = 18
print(xie.age)
print(xie.name)

yu = Student()
print(yu.name)
print(yu.age)

yu.name = "yu"
print(yu.name)
print(yu.age)

Student.name = "xie_rong_rong"
c = Student()
print(c.name)