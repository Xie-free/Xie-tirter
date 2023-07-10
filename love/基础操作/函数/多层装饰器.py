"""
如果装饰器是多层的谁距离函数最近优先使用哪个装饰器


"""

def zhuang_1(func):
    print("--------- 1_start")

    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print("刷漆")

    print("---------- 1_end")
    return wrapper

def zhuang_2(func):
    print("------------ 2_start")

    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print("装地板")

    print("--------- 2_end")
    return wrapper


@zhuang_2
@zhuang_1
def house():
    print("毛坯房")


house()
# --------- 1_start
# ---------- 1_end
# ------------ 2_start
# --------- 2_end
# 毛坯房
# 刷漆
# 装地板
