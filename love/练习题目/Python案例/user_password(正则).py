import re


def user(password):
    for i in range(0, len(password_)):
        pa_str = password_[i]
        patter = re.compile("(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[0-9]).{6,12}")
        result = patter.match(pa_str)
        try:
            result_ = result.group(0)
            if result_:
                return result_
        except AttributeError:
            print(f"{pa_str}不符合规则")
        i += 1
    else:
        return "没有规范密码"


if __name__ == '__main__':
    password_ = input("请输入密码(用逗号分割):").split(",")
    print(user(password_))
