# 装饰器带参数
"""
带参数的装饰器是三层的
最外层的函数负责接受装饰器参数
里面的内容还是原装饰器的内容
"""
def outer(a):   # 第一层: 负责接收参数
    def decorate(func):   # 第二层: 负责接受函数
        def wrapper(*args, **kwargs):   # 第三层: 负责接受函数的实参
            func(*args, **kwargs)
            print(f"铺地板{a}块")

        return wrapper  # 返出来的是第三层

    return decorate     # 返出来的是第二层


@outer(10)
def house(time):
    print(f"我{time}时间拿到房子的钥匙,是毛坯房")


@outer(100)
def street():
    print(f"新修街道名字是:黑泉路")


house("2022-04-01")

street()
