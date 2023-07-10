# 列表升序

# 自己封装一个升序函数

def max_number(list1):
    for j in range(len(list1) - 1):
        for i in range(len(list1) - 1):
            if list1[i] >= list1[i + 1]:
                list1[i], list1[i + 1] = list1[i + 1], list1[i]
    return list1


list2 = [123, 1, 234, 4, 5, 89, 1, 1, 123]

a = max_number(list2)
print(a)


# 列表降序

def min_number(min_list):
    for j in range(len(min_list) - 1):
        for i in range(len(min_list) - 1):
            if min_list[i] < min_list[i + 1]:
                min_list[i], min_list[i + 1] = min_list[i + 1], min_list[i]
    return min_list


b = min_number(list2)
print(b)
