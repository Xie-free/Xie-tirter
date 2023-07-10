import os

src_path = r"F:\python\python_word"
target_path = r"F:\python\python_word1"


def copy(src_path, target_path):
    # 获取文件夹里面内容
    file_list = os.listdir(src_path)
    # 遍历列表
    for file in file_list:
        # 拼接路径
        path = os.path.join(src_path, file)
        # 判断是文件夹还是文件
        if os.path.isdir(path):
            # 重复操作, 可进行递归
            # os.chidir(path)
            # file_list1 = os.listdir(path)
            # for file in file_list1:
            #     path = os.path.join(src_path, file)
            # 递归调用
            copy(path, target_path)
        else:
            # 不是文件夹则直接进行复制
            with open(path, "rb") as r_stream:  # 建立通道
                container = r_stream.read()  # 读取数据
                path1 = os.path.join(target_path, file)  # open只能打开指定文件, 所以制作一个绝对路径
                with open(path1, "wb") as w_stream:
                    w_stream.write(container)  # 把目标文件写入指定目录
    else:
        print("复制完成!")

# 调用函数
copy(src_path, target_path)
