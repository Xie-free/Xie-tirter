"""
游戏:掷骰子
游戏规则
1.玩游戏要有金币,没有就不能玩游戏
2.玩一局赠金币1枚,充值获取金币
3.充值金额为10的倍数,例:充值10元给 20 金币
4.玩游戏消耗金币,一局消耗5个金币
5.猜大小: 猜对  鼓励金币2枚   猜错没金币
6.一局投两个骰子,大小为两个骰子相加, 超出6点以上认为大，否则小
6.游戏结束:   1.主动退出    2.没有金币退出
7. 只要退出则打印金币, 共玩了几局
"""
import random

Gold_coins = random.randint(5, 100)
i = 0
print(f"您的金币数量为: {Gold_coins} ", )
while Gold_coins > 0:
    inquires = input("请问是否要开始游戏,需要花费您5枚金币,再赠送1枚:    (y/n)")
    if inquires == "y":
        Gold_coins -= 5
        Gold_coins += 1
        if Gold_coins >= 0:
            print("----------------开始游戏----------------")
            i += 1
            print(f"您现在金币为：{Gold_coins} ")
            Dice1 = random.randint(1, 6)
            Dice2 = random.randint(1, 6)
            Guess = input("请猜测大小:")
            Dice3 = Dice1 + Dice2
            if Guess == "大":
                if Dice3 > 6:
                    print(f"第一个骰子数为{Dice1}, 第二个骰子数为{Dice2}, 和为{Dice3}")
                    print("大")
                    Gold_coins += 2
                    print(f"您现在金币为：{Gold_coins} ")
                    inquires1 = input("请问是否退出游戏     (y/n)")
                    if inquires1 == "y":
                        print("正在为您退出游戏")
                        break
                elif Dice3 <= 6:
                    print(f"第一个骰子数为{Dice1}, 第二个骰子数为{Dice2}, 和为{Dice3}")
                    print("小")
                    print(f"您现在金币为：{Gold_coins} ")
                    inquires1 = input("请问是否退出游戏     (y/n)")
                    if inquires1 == "y":
                        print("正在为您退出游戏")
                        break

            if Guess == "小":
                if Dice3 > 6:
                    print(f"第一个骰子数为{Dice1}, 第二个骰子数为{Dice2}, 和为{Dice3}")
                    print("大")
                    print(f"您现在金币为：{Gold_coins} ")
                    inquires1 = input("请问是否退出游戏     (y/n)")
                    if inquires1 == "y":
                        print("正在为您退出游戏")
                        break

                elif Dice3 <= 6:
                    print(f"第一个骰子数为{Dice1}, 第二个骰子数为{Dice2}, 和为{Dice3}")
                    print("小")
                    Gold_coins += 2
                    print(f"您现在金币为：{Gold_coins} ")
                    inquires1 = input("请问是否退出游戏     (y/n)")
                    if inquires1 == "y":
                        print("正在为您退出游戏")
                        break
        else:
            print("您的金币不够,已退出游戏")
    elif inquires == "n":
        break

print(f"您现在金币为:{Gold_coins}, 共玩了{i}局")
