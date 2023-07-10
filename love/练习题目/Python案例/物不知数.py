def number(num):
    for i in range(num + 1):
        if i % 3 == 2 and i % 5 == 3 and i % 7 == 2:
            return i


if __name__ == '__main__':
    num_1 = int(input("请输入一个整数"))
    print(number(num_1))
