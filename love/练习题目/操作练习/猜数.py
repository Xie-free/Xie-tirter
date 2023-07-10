import random

a = random.randint(0, 10)
i = 0
while True:
    b = int(input("请输入您要猜的数"))
    i += 1
    if a > b:
        print("数值小了")
    elif a < b:
        print("数值大了")
    elif a == b:
        print("恭喜猜对了")
        break


print(f"您猜了{i}次")
