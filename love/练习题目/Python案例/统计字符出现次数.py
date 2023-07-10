def count_word(str_i):
    dict_count = {}
    for i in str_i:
        if i in dict_count:
            dict_count[i] += 1
        else:
            dict_count[i] = 1
    else:
        a = sorted(dict_count.items(), key=lambda values: values[1])
        num_1 = -1
        count = 0
        number = 0
        flag = 1
        while flag:
            if a[-1][-1] == a[num_1 - 1][-1]:
                num_1 -= 1
            else:
                for i in range(abs(num_1)):
                    number -= 1
                    print(f"{a[number]}")
                else:
                    flag = 0


if __name__ == '__main__':
    str_i_ = input("请输入一串字符串:")
    count_word(str_i_)
