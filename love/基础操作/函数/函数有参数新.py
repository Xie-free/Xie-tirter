"""
参数:
    1. 无参数
    2. 有参数

无参数:
      def 函数名():
    pass
有参数:
      def 函数名(参数1， 参数2， 参数3 ，参数4,.....)
      pass

    参数  就是在调用函数时向函数中传值作用
"""
import random


def generate_code(n):
    # 生成验证码
    s = "asdfalksjdhfakjdhsadkjlfhvasdfzxcv12334213419879182730"
    code = ""
    for i in range(n):
        r = random.choice(s)
        code += r
    print(code)


# 调用函数
generate_code(5)

generate_code(9)


def login(n):
    a = 0
    while a < n:
        use_name = input("用户名")
        use_password = input("密码")
        if use_name == "aaa" and use_password == "123":
            print("登陆成功")
        else:
            print("登陆失败")
            a += 1


login(4)
