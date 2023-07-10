# 引用
import os


# 创建文件夹
# os.mkdir("F:/操作实验2")
#
# # 创造文档
# for i in range(100):
#     os.chdir("F:/操作实验2")
#     f = open(f"{i}.txt", "w")
#     f.write("")
#     f.close()

# 提取文档
files = os.listdir("F:/操作实验2")

for i in files:
    portion = os.path.split(i)
    print(portion)

    if portion[1] == ".txt":
        new_name = portion[0] + "".jpg


        os.chdir("F:/操作实验")
        os.rename(i, new_name)







