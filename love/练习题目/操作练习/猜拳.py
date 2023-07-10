import random
# a是玩家 b 是电脑
b = random.randint(0, 2)
i = 0
while i < 3:
    a = int(input("请出拳：0--石头:1--剪刀：2--布"))
    print(f"电脑出的是0-石头:1-剪刀：2-布      {b}")
    if (a == 0) and (b == 1) or (a == 1) and (b == 2) or (a == 2) and (b == 0):
        print("玩家获胜")
    elif a == b:
        print("平局")
    else:
        print("电脑胜利")
    i += 1

print(a)
