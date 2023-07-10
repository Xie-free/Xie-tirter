# 私有化
# 封装: 1. 私有化属性 2. 定义公有set 和 get 方法
# __属性: 就是将属性私有化, 访问范围仅仅限类中
"""
好处:
1. 隐藏属性不被外界随意修改
2. 也可以修改: 通过函数
    def setXXX(self, xxx):
        3. 筛选赋值的内容
            if xxx 是否符合条件
                赋值
            else:
                不赋值
3. 如果想获取具体的某一个属性
    使用get函数
        def getxxx(self, xxx):
            return self.__xxx  ``` 


"""


class Student:
    __age = 16  # 类属性

    def __init__(self, name, age):
        self.__n = name  # 长度必须6位
        self.__a = age
        self.__score = 12

    # 定义公有set 和 get 方法
    # set 为了赋值
    def set_age(self, a):
        if a > 0 and a < 100:
            self.__a = a
        else:
            print("年龄不在规定范围内")

    # get是为了取值
    def get_age(self):
        return self.__a

    # 修改名字的时候, 必须是6位
    def set_name(self, n):
        if len(n) == 6:
            self.__n = n
        else:
            print("名字不是6位")

    def get_name(self, n):
        return self.__n


    def __str__(self):
        return f"姓名是:{self.__n}, 年龄是{self.__a}, 考试分是{self.__score}"

    # attribute: set_name get_name __init__ __str__

xie = Student("xie", 16)
print(xie)
xie.set_age(180)
print(xie)
xie.set_name("xiexie")

yu = Student("yu", 16)
print(yu)

# 就想拿到谢的年龄
print(xie.get_age())
xie.a = 17
# print(xie.__score)
xie.__score = 15
print(xie)

print(dir(Student))  # 类

# print(xie.__name)  # _Student__n
# print(xie._Student__n)  # 其实它就是__n, 只不过系统自动改名了
print(xie.__dir__)

print(dir(xie))

