# import types  # 导入模块


# 定义类
# class A:
#     def __init__(self, value1=0, value2=0):
#         self._value1 = value1  # 定义私有成员
#         self.__value2 = value2
#
#     def set_value(self, value1, value2):  # 定义方法
#         self._value1 = value1
#         self.__value2 = value2
#
#     def show(self):
#         print(self._value1)
#         print(self.__value2)
#
#
# a = A()  # 创建对象
# # a.show()  # 调用方法
# print(a._value1)
# print(a._A__value2)  # 外部访问私有成员的方法


# class Car(object):
#     price = 1000  # 属于类的数据成员
#
#     def __init__(self, c):
#         self.color = c  # 属于对象的数据成员
#
#
# car1 = Car("Red")  # 实例化对象
# car2 = Car("Blue")
# print(car1.color, Car.price)  # 访问对象和类的数据成员
# Car.price = 110000  # 修改类的数据成员
# Car.name = "QQ"  # 动态增加类的数据成员
# car1.color = "Yellow"  # 修改实例的属性
# print(car2.color, Car.price, Car.name)
# print(car1.color, Car.price, Car.name)
#
#
# def set_Speed(self, s):
#     self.speed = s
#
#
# car1.setSpeed = types.MethodType(set_Speed, car1)  # 动态为对象增加成员方法
# car1.setSpeed(50)  # 传参
# print(car1.speed)


# class Demo(object):  # 创建类
#     total = 0  # 属于类的数据成员
#
#     def __new__(cls, *args, **kwargs):  # 传入的参数
#         if cls.total >= 3:  # 判断
#             raise Exception("Can only create up to 3 objects")  # 抛出异常
#         else:
#             return object.__new__(cls)  # 返回一个类的对象
#
#     def __init__(self):  # 执行完__new__后会执行__init__()
#         Demo.total = Demo.total + 1  # 对类的数据成员进行加一
#
#
# t1 = Demo()  # 实例化对象
# print(t1)
# try:
#     t2 = Demo()
#     t3 = Demo()
#     t4 = Demo()
# except Exception as e:
#     print(repr(e))
# print(t4)
# class Root:  # 创建类
#     __total = 0  # 创建私有化类数据成员
#
#     def __init__(self, v):  # 构造方法
#         self.__value = v  # 创建属于对象的私有化数据成员
#         Root.__total += 1  # 私有化的类数据加一
#
#     def show(self):
#         print("self.__value:", self.__value)
#         print("Root.__total:", Root.__total)
#
#     @classmathod  # 修饰器, 声明类方法
#     def class_show_total(cls):  # 类方法
#         print("cls.__total:", cls.__total)
#
#     @staticmethod  # 修饰器, 声明静态方法
#     def static_show_total():  # 静态方法
#         print("Root.__total", Root.__total)
#
#
# r = Root(3)  # 实例化对象
# r.class_show_total()  # 通过对象来调用类方法
# r.static_show_total()  # 通过对象来调用静态方法
# r.show()  # 调用方法
# print("-" * 50)
#
# rr = Root(5)
# rr.class_show_total()
# rr.static_show_total()
# rr.show()
# print("-" * 50)
#
# Root.class_show_total()  # 通过类名调用类方法
# Root.static_show_total()  # 通过类名调用静态方法
# print("-" * 50)
#
# # Root.show()  # 试图通过类名直接调用实例方法,失败
# Root.show(r)  # 但是可以通过这种方法来调用方法并访问实例成员

# class Demo:
#     pass
#
#
# t = Demo()
#
#
# def test(self, v):
#     self.value = v
#
#
# t.test = test
# print(t.test)  # 动态增加普通函数
# t.test(t, 3)
# print(t.value)
# import types
#
# t.test = types.MethodType(test, t)  # 动态增加绑定的方法
# t.test(5)
# print(t.test(5))

# class Test:
#     def __init__(self, value):
#         self.__value = value
#
#     @property
#     def vaule(self):  # 只读,无法修改和删除
#         return self.__value
#
#
# t = Test(3)
# print(t.vaule)
#
# # t.vaule = 5  # 只读属性不允许修改值,不然会报错
# t.v = 5  # 动态增加新成员
# print(t.v)
# del t.v  # 动态删除成员
# # del t.vaule  # 试图删除对象属性,失败,会报错
# print(t.vaule)

# class Test:
#     def __init__(self, value):
#         self.__value = value
#
#     def __get(self):  # 读取私有数据成员的值
#         return self.__value
#
#     def __set(self, v):  # 修改私有数据成员的值
#         self.__value = v
#
#     value = property(__get, __set)  # 可读可写属性,指定相应的读写方法
#
#     def show(self):
#         print(self.__value)
#
#
# t = Test(3)
# print(t.value)  # 允许读取属性值
#
# t.value = 5  # 允许修改属性值
# print(t.value)
#
# t.show()  # 属性对应的私有变量也得到了相应的修改
#
# # del t.value  # 试图删除属性,失败了

# class Test:
#     def __init__(self, value):
#         self.__value = value
#
#     def __get(self):
#         return self.__value
#
#     def __set(self, v):
#         self.__value = v
#
#     def __del(self):
#         del self.__value
#
#     value = property(__get, __set, __del)
#
#     def show(self):
#         print("self.value",self.value)
#
#
# t = Test(3)
# t.show()
#
# print(t.value)
#
# t.value = 5
# t.show()
#
# print(t.value)
#
# del t.value  # 删除属性
# # t.value  # 对应的私有数据成员已被删除
# # t.show()
#
# t.value = 1  # 为对象动态增加属性和对应的私有数据成员
# t.show()
#
# print(t.value)
