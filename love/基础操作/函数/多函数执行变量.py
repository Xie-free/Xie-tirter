# 1. 定义全局变量
glo_num = 0


def test1():
    global glo_num
    glo_num = 100


def test2():
    print(glo_num)


print(glo_num)  # 0

test2()  # 0

test1()

test2()  # 100
