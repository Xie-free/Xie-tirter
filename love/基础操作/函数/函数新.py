"""
图书管理:
借书 ---> 查询  书
还书 ---> 查询  书
查询

函数: 复用

参数可有可无
格式 函数名([参数,.....]):
     代码

函数名:get_name()
      search()
代码:
    封装重复内容
调用函数:  函数名 + ()
"""
import random


def generate_code():
    # 生成验证码
    s = "asdfalksjdhfakjdhsadkjlfhvasdfzxcv12334213419879182730"
    code = ""
    for i in range(4):
        r = random.choice(s)
        code += r
    print(code)


print(generate_code)  # <function generate_code at 0x000001CCFBB94180>

# 验证函数是否可用?  调用函数
generate_code()

"""
定义一个login函数:
输入用户名和密码,验证是否正确

"""


def login():
    use_name = input("用户名")
    use_password = input("密码")
    if use_name == "aaa" and use_password == "123":
        print("登陆成功")
    else:
        print("登陆失败")


login()