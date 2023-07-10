# 列表的最大值
list1 = [1, 4, 546, 66, 95, 43, 3, 1, 1, 1, 1, 1, 4, 5, 6, 12312, 0.5]


def max_number(max_list):
    a = max_list[0]
    for i in max_list:
        if a < i:
            a = i
    return a


result = max_number(list1)
print(result)


# 列表最小值
def min_number(min_list):
    a = min_list[0]
    for i in min_list:
        if a > i:
            a = i
    return a


result = min_number(list1)
print(result)
