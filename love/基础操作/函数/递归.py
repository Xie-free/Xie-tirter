# 回顾函数返回值：写法 和 返回的位置:函数调用的位置
def return_num():
    return 100


result = return_num()
print(result)

# 需求:3以内数字累加和 3 + 2 + 1 = 6
# 6 = 3 + 2以内数字累加和
# 2以内数字累加和 = 2 + 1 以内数字累加和
# 1以内数字累加和= 1


def sum_number(num):
    # 2. 出口
    if num == 1:  # 如果没有出口,报错：超出最大递归深度
        return 1
    # 1. 当前数字 + 当前数字减一的累加和
    return num + sum_number(num-1)


love = sum_number(3)
print(love)



