# 文件的复制
"""
原文件: F:\python_word\quan.png
目标文件: F:\python_word1\quan.png

with 结合open使用, 可以帮助我们自动释放资源

"""
# stream = open("F:\python_word", "rb")


with open(r"F:\python_word\quan.png", "rb") as stream:
    container = stream.read()  # 读取文件内容

    with open(r"F:\python_word1\quan.png", "wb") as w_stream:
        w_stream.write(container)

print("文件复制完成")




