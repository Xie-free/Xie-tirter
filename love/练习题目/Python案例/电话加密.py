def phone_encryption(number):  # 接受一个整数
    if len(str(number)) != 4:  # 判断位数
        return "请输入四位整数"
    else:
        str_number = str(number)  # 将整数转换成字符串
        number_list = []  # 创建一个空列表
        for i in str_number:  # 遍历获取每个子符
            i = (int(i) + 5) % 10  # 将子符转成整数并加5,再与10取余
            number_list.append(i)  # 添加列表
        else:
            number_list[0], number_list[3] = number_list[3], number_list[0]
            number_list[1], number_list[2] = number_list[2], number_list[1]
            result_str = ""
            for i in number_list:
                result_str = result_str + str(i)
            else:
                return int(result_str)


if __name__ == '__main__':
    number_ = int(input("请输入一个四位整数"))
    print(phone_encryption(number_))
