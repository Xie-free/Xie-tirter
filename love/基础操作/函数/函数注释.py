"""
函数的注释:
def 函数名(参数1,....):
    # 基本注释   " 注释内容"
    高级注释
    '''
    函数说明

    参数说明:
    :param user_name:  用户名
    :param password:   用户登录密码

    返回值说明
    :return:  是否登录成功
    '''

"""


def login(user_name, password):
    """
    :param user_name:  用户名
    :param password:   用户登录密码
    :return:  是否登录成功
    """
    if user_name == "xie" and password == 520:
        print("登录成功")
        return True
    else:
        print("输入错误")


login("xie", 520)
