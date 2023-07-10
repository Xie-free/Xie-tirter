def prime(number):
    ls = []
    if number <= 2:  # 如果正整数不大于2直接输出2
        print(2)
    elif number > 2:
        for num in range(2, number + 1):
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                ls.append(num)
        else:
            return ls


if __name__ == '__main__':
    number_is = int(input("请输入一个正整数"))
    print(prime(number_is))
