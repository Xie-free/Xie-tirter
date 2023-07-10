def str_l(m_, n_, str_c_):
    li = []
    for i in str_c_:
        sum_str = 0
        for v in str_c_[::-1]:
            if i == v:
                sum_str += 1
        else:
            if sum_str == n_:
                li.append(i)

    return li[m_-1]


if __name__ == '__main__':
    m, n = map(int, input("请输入第m个只出现过n次的字符").split())
    str_c = input("请输入字符串")
    print(str_l(m, n, str_c))
