# 模块: xxx.py
import random
"""
os.path:
os.path.dirname(__file__)获取当前文件所在的文件目录(绝对路径)  # file表示当前目录
os.path.join(path, "")  返回的是一个拼接后的新的路径

"""

import os

# print(os.path)
# path = os.path.dirname(__file__)  # 获取当前文件所在的文件目录(绝对路径)
# print(path)
# print(type(path))
# result = os.path.join(path, "quan.png")
# print(result)

# p1\quan.png ----->保存在当前文件所在目录
with open(r"F:\python\python_word\quan.png", "rb") as stream:
    container = stream.read()  # 读取文件内容
    print(stream.name)  # F:\python_word\quan.png
    file = stream.name
    file_name = file[file.rfind("\\") + 1:]  # 截取文件名
    path = os.path.dirname(__file__)
    result = os.path.join(path, file_name)
    with open(result, "wb") as w_stream:
        w_stream.write(container)
