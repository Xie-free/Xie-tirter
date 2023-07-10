# 公鸡五元一只, 母鸡三元一只, 小鸡一元3只.
# 用户输入想买的鸡的数量和付出的钱数,
# 计算公鸡、母鸡、小鸡的数量
# 如果有解,输出公鸡最少,小鸡最多的一组;
# 如果无解则输出无解
def chick(money, number):
    for cock in range(1, number):
        for hen in range(1, number):
            chick_1 = number - cock - hen
            if chick_1 % 3 == 0 and chick_1 > 0 and cock * 5 + hen * 3 + chick_1 // 3 == money:
                return f"公鸡:{cock}只, 母鸡{hen}只, 小鸡{chick_1}只"

    else:
        return "无解"


if __name__ == '__main__':
    money, number = map(int, (input("请输入钱和鸡:").split()))
    print(chick(money, number))
