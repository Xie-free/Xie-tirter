import os

# 文件复制
src_path = r"F:\python\python_word"
target_path = r"F:\python\python_word2"


# 封装成函数
def copy(src, target):
    if os.path.isdir(src) and os.path.isdir(target):  # 判断是否为一个文件夹
        file_list = os.listdir(src)  # ["aa.txt".....]
        for file in file_list:  # 遍历获取文件夹名字
            path = os.path.join(src, file)  # 获取目标文件夹绝对路径
            with open(path, "rb") as r_stream:  # 建立通道
                container = r_stream.read()  # 读取数据
                path1 = os.path.join(target, file)  # open只能打开指定文件, 所以制作一个绝对路径
                with open(path1, "wb") as w_stream:
                    w_stream.write(container)  # 把目标文件写入指定目录
        else:
            print("复制完毕")


# 调用函数
copy(src_path, target_path)
