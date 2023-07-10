def fei_bo(n):
    a, b = 1, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b


if __name__ == '__main__':
    n_ = int(input("请输入到斐波那契数列第几项:"))
    fei_bo(n_)