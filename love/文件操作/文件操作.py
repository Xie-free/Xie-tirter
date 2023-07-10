"""
1. 导入模块os
2.使用模块功能
"""

import os

# 1. rename(): 重命名
# os.rename('2[备份].txt', "即将删除.txt")

# 2. remove(): 删除文件
# os.remove("即将删除.txt")

# 3. mkdir(): 创建文件夹
# os.mkdir("F:/aa")

# 4. rmdir(): 删除文件夹
# os.rmdir("")

# 5. getcwd(): 返回当前文件所在目录
# print(os.getcwd())

# 6. chdir(): 改变默认目录
# 需求: 在aa里面创建bb文件夹; 1. 切换目录到aa, 2. 创建bb
# os.chdir("F:/aa")
# os.mkdir("bb")

# 7. listdir(): 获取目录列表
# print((os.listdir()))


# 8. rename(): -- 重命名文件夹
# os.rename("F:/ce2", "即将删除")


"在F:盘创建一个文件夹, 里面包含1到100"
# for i in range(100):
#     if i == 0:
#         os.mkdir("F:/操作实验")
#
#     os.chdir("F:/操作实验")
#     os.mkdir(f"{i}")


