def list_index(list_, num_1, num_2):
    list_ = list(list_)
    return list_[num_1:num_2 + 1]


if __name__ == '__main__':
    list_i = eval(input("请输入一个列表:"))
    num_1_, num_2_ = map(int, input("请输入两个整数作为下表索引:").split())
    print(list_index(list_i, num_1_, num_2_))
