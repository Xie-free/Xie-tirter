def hundred_divisible(input_str):
    return input_str // 100


if __name__ == '__main__':
    input_str_ = int(input("请输入一个三位以上的整数:"))
    print(hundred_divisible(input_str_))