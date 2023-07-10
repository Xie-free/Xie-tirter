# 输入一个正整数n,判断1和n之间是否存在3和5的公倍数
# 若有,则输出最小的一个
# 若无,则输出n以内没有3和5的公倍数
def multiple(x):
    for i in range(1, x):
        if i % 3 == 0 and i % 5 == 0:
            return i
    else:
        return "n以内没有3和5的公倍数"


if __name__ == '__main__':
    try:
        n = int(input("请输入一个正整数"))
        print(multiple(n))
    except ValueError:
        print("请输入正整数")

