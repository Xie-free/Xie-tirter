def list_index(i_list, num_1, num_2):
    count = -1
    r_list = []
    for i in i_list:
        count += 1
        if count <= num_2:
            if count >= num_1:
                r_list.append(i)
    else:
        return r_list


if __name__ == '__main__':
    i_list_ = eval(input("请输入一个列表:"))
    num_1_, num_2_ = map(int, input("请输入两个整数作为下标索引:").split())
    print(list_index(i_list_, num_1_, num_2_))