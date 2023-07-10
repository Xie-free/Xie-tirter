def hundred(str_input):
    if len(str_input) > 3:
        hundred_number = str_input[0:-3]
        return int(hundred_number)
    elif len(str_input) == 3:
        return int(str_input[0])
    elif len(str_input) < 3:
        return f"{str_input}不满足条件"


if __name__ == '__main__':
    str_input_ = input("请输入一个三位以上的整数:")
    print(hundred(str_input_))
