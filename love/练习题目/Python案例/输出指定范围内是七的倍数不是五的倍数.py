def scope(n, m):
    list_number = []
    for i in range(n, m):
        if (i % 7 == 0) and (i % 5 != 0):
            list_number.append(i)
    else:
        for i in list_number:
            print(f"{i}", end=",")


if __name__ == '__main__':
    n_, m_ = map(int, input("请输入两个整数作为指定范围:").split())
    scope(n_, m_)