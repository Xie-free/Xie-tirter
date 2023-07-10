# 文件操作:
"""
文件上传
保存log

系统函数:
    open(file, mode, buffering, encoding)

读:
    open(path/filename, "rt")  ----> 返回值: steam(管道)

    container = stream.read()  ----> 读取管道的内容

    注意: 如果传递的path/filename有误, 则会报错: FileNotFoundError
    如果是图片则不能是用默认读取方式, mode = "rb"

    总结:
    read()  读取所有内容
    readline()  每次读取一行内容
    readlines()  读取所有的行保存到列表中
    readable()  判断是否可读
"""
# 此处r是防止\被误解为转移字符
stream = open(r"F:\python_word\a.TXT")

# container = stream.read()
# print(container)

result = stream.readable()  # readable判断是否可以读取  Turn False
print(result)

line = stream.readline()  # 如上边有stream.read表示读取完了, readline读取不到
print(line)

# while True:
#     line = stream.readline()
#     print(line)
#     if not line:
#         break

lines = stream.readlines()  # 保存到列表中
print(lines)

for i in lines:
    print(i)


stream = open(r"F:\python_word\quan.png", "rb")
container = stream.read()
print(container)
