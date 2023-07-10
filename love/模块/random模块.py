# random 模块

import random

ran = random.random()  # 0-1 之间的随机小数
print(ran)

ran_1 = random.randrange(1, 10, 2)  # randrange(start, stop, step)  1~10 step=2  ---> 1,3,5,7,9
print(ran_1)

ran_1 = random.randrange(1, 10)
print(ran_1)

ran_2 = random.randint(1, 10)
print(ran_2)

list1 = ["xie", "hei", "rong", "yu", "deng"]
ran = random.choice(list1)  # 随机选择列表的内容
print(ran)

pai = ["红桃A", "方片K", "梅花8", "黑桃9"]
random.shuffle(pai)  # 打乱列表顺序
print(pai)


# 验证码  大写字母与数字的组合
def func():
    code = ""
    for i in range(4):
        ran1 = str(random.randint(0, 9))
        ran2 = chr(random.randint(65, 90))
        ran3 = chr(random.randint(97, 122))

        r = random.choice([ran1, ran2, ran3])

        code += r

    return code

code = func()
print(code)