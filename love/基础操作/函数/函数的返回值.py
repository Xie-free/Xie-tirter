def test1():
    return 1
    return 2


return_num = test1()

print(return_num)


def test2():
    # return 1, 2  # 返回的是元组
    # return 后面可以直接书写 元组 列表 字典, 返回多个值
    # return[10, 20]  # 返回的是列表
    return {"name": "xie", "age": 10}


return_num1 = test2()

print(return_num1)
