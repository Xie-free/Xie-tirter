def login_password(password):
    for i in password:  # 遍历获取密码
        str_big_word = 0  # 定义变量
        str_small_word = 0
        str_number = 0
        str_fu_hao = 0
        for b in i:  # 遍历密码的每一个字母
            if 65 <= ord(b) <= 90:  # 与ascii码进行判断
                str_big_word += 1
            elif 97 <= ord(b) <= 122:
                str_small_word += 1
            elif 48 <= ord(b) <= 57:
                str_number += 1
            elif (ord(b) == 36) or (ord(b) == 35) or (ord(b) == 64):
                str_fu_hao += 1
        else:  # 正常运行结束后
            if (str_big_word >= 1) and (str_small_word >= 1) and (str_number >= 1) and (str_fu_hao >= 1):
                # 判断是否都有
                if 6 <= len(i) <= 12:
                    # 长度判断
                    return i


if __name__ == '__main__':
    password_ = input("请输入密码(逗号分割):").split(",")
    print(login_password(password_))
