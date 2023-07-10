def factor(m):
    n = m
    number_lis = []
    while m != 1:
        for i in range(2, int(m + 1)):
            if m % i == 0:
                m = m / i
                number_lis.append(i)
    else:
        print(f"{n} = ", end="")
        number_lis.sort()
        for number in number_lis:
            if number == number_lis[-1]:
                print(f"{number}", end="")
            else:
                print(f"{number} * ", end="")


if __name__ == '__main__':
    m_ = int(input("请输入一个正整数:"))
    factor(m_)
