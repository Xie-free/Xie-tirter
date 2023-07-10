# 1.	读取7个数（1—50）的整数值，每读取⼀个值，程序打印出该值个数的*
from random import sample  # 导入random里的sample函数.


def print_str():
    number_list = list(range(1, 51))  # 获取1-50的数.
    result_list = sample(number_list, 7)  # 从1-50里取7个整数值.
    for i in result_list:  # 遍历获取数值
        print("*" * i, i)  # 打印


if __name__ == '__main__':
    print_str()
