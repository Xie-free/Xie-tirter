# 猫
class Cat:
    type = "猫"

    # 通过__init__初始化的特征
    def __init__(self, nick_name, age, color):
        self.nick_name = nick_name
        self.age = age
        self.color = color

    def eat(self, food):
        print(f"{self.nick_name}喜欢吃{food}")

    def catch_mouse(self, color, weight):
        print(f"{self.nick_name}抓了{weight}kg的老鼠, 颜色是{color}")

    def sleep(self, hour):
        if hour < 5:
            print("继续睡会吧")

        else:
            print("起来抓老鼠")

    def show(self):
        print(f"猫的详细信息")
        print(self.nick_name)
        print(self.age)
        print(self.color)


# 创建对象
cat_1 = Cat("小小", 3, "黄色")

# 通过对象调用方法
cat_1.catch_mouse("黑色", 12)

cat_1.sleep(8)

cat_1.eat("鲸鱼")

cat_1.show()

