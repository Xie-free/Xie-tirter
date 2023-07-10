# 开发: 登录验证
import time

is_login = False  # 默认是没有登录的


# 定义一个登录函数
def login():
    user_name = input("请输入用户名:")
    password = input("请输入密码:")
    if user_name == "xie" and password == "1234":
        return True
    else:
        return False


# 定义一个装饰器, 进行付款验证 n
def login_required(func):
    def wrapper(*args, **kwargs):
        global is_login
        print("---------付款-----------")
        # 验证用户是否登录
        if is_login:
            func(*args, **kwargs)
        else:
            # 跳转登录页面
            print("用户没有登录, 不能付款")
            is_login = login()
            print("result:", is_login)

    return wrapper


@login_required
def pay(money):
    print(f"正在付款, 付款金额是:{money}元")
    print("付款中")
    time.sleep(2)
    print("付款完成!")


pay(10000)
pay(8000)
