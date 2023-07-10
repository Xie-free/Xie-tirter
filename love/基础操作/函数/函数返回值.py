"""
参数: 外界向里面传值
返回值: 里面的内容向外界传送

def 函数名(参数,......):
    .....
    .....
    return xxxx
当函数调用时通过return向外返出值.
注意: 只要函数有返回值,则需要变量来接收

return 后面的值可以是一个值, 也可以史多个值.
如果史多个值 类似: return a, b, c 会将多个返回值存进元组中
将元组作为整体返回
结果:(a, b, c)
"""


def get_sum(*args):
    n = 0
    for i in args:
        n += i
        # 将n 返回
    return n


n = get_sum(1, 2, 3, 4, 5)
x = 100
x = x + n
print(x)


def get_max_min(numbers):  # num
    # 先排序:冒号排序
    for i in range(len(numbers) - 1):
        for j in range(len(list1) - 1 - i):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    print(numbers)
    #  获取头,尾
    min = numbers[0]
    max = numbers[-1]
    # 返出
    return min, max  # (min, max)


list1 = [1, 123, 45345, 675, 45, 75, 78, 34, 68, 5456, 90]

result = get_max_min(list1)
print(result)

min_1, max_1 = get_max_min(list1)
# a,b = (1, 2)
print(min_1)
print(max_1)
