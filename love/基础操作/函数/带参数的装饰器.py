"""
带参数的装饰器:
如果原函数有参数则装饰器内部函数也要有参数.


"""


def decorater(func):
    def wrapper(*args, **kwargs):  # address = "北京四合院"
        # args 是一个元组
        func(*args, **kwargs)  # func就是house
        print("刷漆")
        print("铺地板")
        print("买房具")
        print("精修房子")

    return wrapper


@decorater
def house(address):
    print(f"房子的地址在:{address}是一个毛坯房")


@decorater
def chang_fang(address, area):
    print(f"房子的地址在:{address}是一个毛坯房,建筑面积是{area}平方米")


@decorater
def hotel(name, address, area=40):
    print(f"酒店的名字是:{name},地址在:{address}是一个毛坯房,建筑面积是{area}平方米")


house("北京四合院")  # house 就是wrapper

print("---------------")

chang_fang("北京沙河北大桥", 100)

hotel("全季大酒店", "北京国贸")
