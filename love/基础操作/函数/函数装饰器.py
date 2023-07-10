"""
装饰器:
遵循开放封闭原则, 在不改变原函数的情况下, 扩展了函数的功能

定义:
def xxx(func):
    def xxx(参数,...):
        .....
        func()
        ....
        return yyy
    return xxx

装饰:
@装饰器名    ----> 原函数 = 装饰(原函数)
def 原函数():
    pass

装饰器(decorator)功能:
引用日志
函数执行时间统计
执行函数前预备处理
执行函数后清理功能
权限校验等场景
缓存

"""


# 定义装饰器
def decorater(func):
    print("------------------->")
    def wrapper():
        func()
        print("刷漆")
        print("铺地板")
        print("买房具")
        print("精修房子")

    return wrapper

@decorater  # house = decorate(house)
def house():
    print("毛坯房....")

house()

# def foo():
#     print("foo")
#
#
# def func():
#     print("func")
#
#
# foo = func
# foo()
