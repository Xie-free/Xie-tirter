"""
装饰器修饰有返回值函数
原函数有返回值, 装饰器的内部函数也要有返回值


"""


def decorater(func):  # function 函数
    def wrapper(*args, **kwargs):
        r = func(*args, **kwargs)
        print(f"预计装修费用:{r}")
        print("刷漆")
        print("铺地板")
        print("买房具")
        print("精修房子")
        return 6000

    return wrapper


@decorater
def house():
    print("我是一个毛坯房...")
    return 5000


r = house()  # house  就是wrapper
print(r)
