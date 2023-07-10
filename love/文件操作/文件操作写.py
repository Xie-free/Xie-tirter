# 写文件
"""
stream = open(r"F:\python_word\a.TXT", "w")
mode 是"w"  表示就是写操作  每次都会将原来的内容清空

方法:
    write(内容)   , 然后写当前的内容
    writelines(Iterable(可迭代))   没有换行效果
    stream.writelines(["赌神: 高进\n", "赌侠: \n", "赌圣: 周星星\n"])

如果 mode = "a"

"""

stream = open(r"F:\python_word\a.TXT", "a")

# s = """
# 你好!
#     欢迎来到澳门博彩赌场, 赠送给你一个金币!
#                 赌王: 高进
#
# """

result = stream.write("hell")
print(result)

stream.write("龙五")

stream.writelines(["赌神: 高进\n", "赌侠: \n", "赌圣: 周星星\n"])

stream.write("僵尸先生")

stream.close()  # 释放资源

# stream.write("龙二")