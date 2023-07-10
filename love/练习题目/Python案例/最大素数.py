# 用户输入一个大于1的正整数n, 计算并输出不大于n的最大的素数.
def prime(n):
    for i in range( + 1, 3, -1):
        for a in range(2, i):
            if i % a == 0:
                break
        else:
            return i


if __name__ == '__main__':
    x = int(input("请输入一个大于1的正整数"))
    print(prime(x))
