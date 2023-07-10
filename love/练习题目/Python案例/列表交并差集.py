# 求两个列表的交集、差集、并集def diff(listA,listB):

def diff(list_a, list_b):
    intersection_list = []  # 交集列表
    difference_list = []  # 差集列表
    for x in list_a:  # 遍历获取元素
        if x in list_b:  # 判断
            intersection_list.append(x)  # 如果在交集列表就要加上
    else:
        for i in list_b:  # 遍历b的元素
            list_a.append(i)  # 相加在a上
        else:
            list_a = set(list_a)  # 转换成集合去重
    for d in list(list_a):  # 遍历并集的元素
        if d not in intersection_list:  # 如果不在交集里
            difference_list.append(d)  # 就一定是差集
    return f"并集是:{list(list_a)}\n交集是:{intersection_list}\n差集是:{difference_list}"


if __name__ == '__main__':
    list_a_ = eval(input("请输入第一个列表"))
    list_b_ = eval(input("请输入第二个列表"))
    print(diff(list_a_, list_b_))
