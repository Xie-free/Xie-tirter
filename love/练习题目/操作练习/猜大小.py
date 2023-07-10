"""
猜数字游戏

Version: 0.1
Author: 骆昊
"""
import random
a = random.randint(1, 100)
counter = 0
while input:
    counter += 1
    number = int(input("请输入："))
    if number < a:
        print("大一点")
    elif number > a :
        print("小一点")
    else :
        print("恭喜你猜对了")
        break
print(f"你总共猜了{counter}次")
if counter > 7:
    print("666")
