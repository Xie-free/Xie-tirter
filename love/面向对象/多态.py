#  封装  继承  多态 ----->>> 面向对象
class Person:
    def __init__(self, name):
        self.n = name

    def feed_pet(self, pet):  # 既可以接受cat, 也可以接受dog, 还可以接受tiger
        # isinstance(类, object)  ------>判断类是不是object的对象或判断类是不是object子类的对象
        if isinstance(pet, Pet):
            print(f"{self.n}喜欢养{pet.role}, 名字是{pet.nick}")
        else:
            print("不是宠物类型")


class Pet:
    role = "Pet"

    def __init__(self, nick_name, age):
        self.nick = nick_name
        self.a = age

    def show(self):
        print(f"宠物名:{self.nick}, 年龄{self.a}")


class Cat(Pet):
    role = "猫"

    def catch_mouse(self):
        print("抓老鼠")


class Dog(Pet):
    role = "狗"

    def watch_house(self):
        print("看家")


class Tiger:
    def eat(self):
        print("吃肉")


# 创建对象
cat = Cat("blue", 5)

dog = Dog("black", 7)

tiger = Tiger()

xie = Person("xie")
xie.feed_pet(cat)
xie.feed_pet(dog)
print("---------------------")

like = Person("like")
like.feed_pet(Tiger)

# Pet 
# pet 父类       cat  dog  子类
# pet 大类型     cat  dog  小类型
