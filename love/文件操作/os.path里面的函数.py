# os.path里面函数
# os中函数:
import os

dir = os.getcwd()  # 当前文件所在的目录
print(dir)

all = os.listdir(r"F:\python\python_word")  # 返回指定目录下的所有文件和文件夹, 保存在列表中
print(all)

# 创建文件夹
if not os.path.exists(r"F:\python\python_word"):
    f = os.mkdir(r"F:\python\python_word2 ")
    print(f)

# f = os.rmdir(r"F:\python_word2")  # 只能删除空的文件夹
# print(f)

# f = os.removedirs(r"F:\python_word2")  # 只能删除空的文件夹
# print(f)

# os.remove(r"F:\python_word2\a.txt")

# 删除asd
# path = r"F:\python_word2\asd"
#
# file_list = os.listdir(path)
# for file in file_list:
#     path1 = os.path.join(path, file)
#     os.remove(path1)
#
# else:
#     os.rmdir(path)
#
# print("删除成功")

# 切换目录
path = os.getcwd()
print(path)

f = os.chdir(r"F:\python")
print(f)

path = os.getcwd()
print(path)

"""
os模块下方法:
os.getcwd()  # 获取当前文件所在目录
os.listdir()  # 浏览文件夹
os.mkdir()  # 创建文件夹
os.rmdir()  # 删除一个空文件夹
os.remove()  # 删除文件
os.chdir()  # 切换目录

"""
