import os


def rename_file_raw(name):
    """
    :return: 对文件进行集体更名并创建一个新的文件夹
             依次把更名后的文件放进对应的文件夹
             文件夹名为文件名
    """
    file_address = r"F:\文件操作\2112计算机考证照片"  # 需要批量更名的文件绝对路径
    file_list = os.listdir(file_address)  # 读取文件
    for i in file_list:  # 遍历获取文件名
        r_file_name = os.path.join(file_address, i)  # 拼接文件的目录
        if os.path.isdir(r_file_name):  # 判断是否为文件夹
            continue  # 跳过本次循环
        file_name = os.path.splitext(i)[0]  # 文件名
        file_type = os.path.splitext(i)[1]  # 文件后缀
        os.mkdir(r"F:\文件操作" + "\\" + file_name)  # 创建一个新的文件夹,名字为文件名
        os.rename(r_file_name, r"F:\文件操作" + "\\" + file_name + "\\" + file_name + f"{name}" + file_type)
        # 拆开解析 第一个参数r_file_name为文件的名字
        # 第二个参数为文件更名后变更的路径,可为绝对路径或者相对路径


def rename_file_change(name):
    """
    :return: 对文件进行集体更名并创建一个新的文件夹
             依次把更名后的文件放进对应的文件夹
             文件夹名为文件名
    """
    file_address = r"F:\文件操作\2112计算机考证照片\更改大小后"  # 需要批量更名的文件绝对路径
    file_list = os.listdir(file_address)  # 读取文件
    for i in file_list:  # 遍历获取文件名
        r_file_name = os.path.join(file_address, i)  # 拼接文件的目录
        if os.path.isdir(r_file_name):  # 判断是否为文件夹
            continue  # 跳过本次循环
        file_name = os.path.splitext(i)[0]  # 文件名
        file_type = os.path.splitext(i)[1]  # 文件后缀
        os.rename(r_file_name, r"F:\文件操作" + "\\" + file_name + "\\" + file_name + f"{name}" + file_type)
        # 拆开解析 第一个参数r_file_name为文件的名字
        # 第二个参数为文件更名后变更的路径,可为绝对路径或者相对路径


if __name__ == '__main__':
    name_ = input("请输入一个参数为文件更名")
    rename_file_raw(name_)
    name_1 = input("请输入一个参数为文件更名(第二个)")
    rename_file_change(name_1)
