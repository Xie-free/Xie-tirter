"""
带多个参数的函数

def 函数名(参数1， 参数2)：
    函数体

"""


# 判断是否是整形   isinstance(变量, 类型)  -----> 返回值是bool
def get_sum(a, b):
    print("函数中:", a, b)
    if isinstance(a, int) and isinstance(b, int):
        s = a + b
        print(s)
    else:
        print("类型错误")


get_sum(2, 3)
get_sum("hell", "world")


# 判断用户是否成功登录
def islogin(user_name, password, isremember=False):
    print("是否记住密码?", isremember)
    if user_name == "aaa" and password == "123":
        print("登录成功")
    else:
        print("登录失败")


islogin("aaa", "123")
