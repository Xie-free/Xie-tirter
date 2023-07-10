def stats(str_1):
    big = 0
    small = 0
    for i in str_1:
        if i.isalpha():
            if 65 <= ord(i) <= 90:
                big += 1
            elif 97 <= ord(i) <= 122:
                small += 1
    return f"大写实例 {big} \n小写实例 {small}"


if __name__ == '__main__':
    str_2 = input("请输入一串句子")
    print(stats(str_2))
