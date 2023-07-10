# 在n的范围之间,与3无关的数
# 不能被3整除,位数上也不能有3
def three(n_):
    lis = []
    for i in range(1, n):
        if i % 3 != 0 and "3" not in str(i):
            lis.append(i)
    else:
        return lis


if __name__ == '__main__':
    n = int(input("请输入范围"))
    print(three(n))
