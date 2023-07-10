# 继承: is a,  has a
import random


# 声明(定义) Road
class Road:
    def __init__(self, name, len):
        self.n = name
        self.l = len


# 声明(定义) Car
class Car:
    def __init__(self, brand, speed):
        self.b = brand
        self.s = speed

    def get_time(self, road):  # road = r   road 与 r指向同一个地址
        ran_time = random.randint(1, 10)
        msg = f"{self.b}品牌的车在{road.n}以{self.s}速度行驶了{ran_time}小时"
        print(msg)

    def __str__(self):
        return f"{self.b}品牌, {self.s}速度"


# 创建实例化对象
r = Road("青藏高速", 1000000)
r.n = "哈尔高速"
car_audi = Car("奥迪", 150)

print(car_audi)
car_audi.get_time(r)  # 对象
