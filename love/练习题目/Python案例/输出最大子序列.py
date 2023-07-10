def series(m):
    empty = []
    l_reverse = m.copy()
    l_reverse.reverse()
    for i in m:
        count_i = m.index(i)
        for contrary in l_reverse:
            count_contrary = l_reverse.index(contrary)
            if (m[count_i] == m[-1]) or (m[count_contrary] == m[1]) \
                    or (l_reverse[count_contrary] == m[1]):
                break
            elif m[count_i + 1] != m[count_contrary - 1] or m[count_i - 1] != m[count_contrary + 1]:
                empty.append(int(i) + int(contrary))
                count_i += 1
                count_contrary += 1
    else:
        return max(empty)


if __name__ == '__main__':
    l_ = list((input("请输入一个列表")).split(","))
    print(l_)
    print(series(l_))
