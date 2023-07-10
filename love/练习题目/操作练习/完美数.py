def perfect_number(n):
    container = []
    for i in range(2, n):
        for a in range(2, n // 2):
            if i != a:
                if i % a == 0:
                    break
            else:
                continue
        else:
            container.append(i)
    else:
        for i in container:
            if (2 ** i - 1) in container:
                print((2**i-1) * (2 ** (i-1)), end=" ")


if __name__ == '__main__':
    n_ = int(input("请输入到第几位的完全数"))
    perfect_number(n_)
