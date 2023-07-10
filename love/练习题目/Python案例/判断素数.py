def is_prime(m):
    for i in range(2, m // 2):
        if m % i == 0:
            return False
    else:
        return True


if __name__ == '__main__':
    m_ = int(input("请输入一个整数判断是否为素数:"))
    print(is_prime(m_))
