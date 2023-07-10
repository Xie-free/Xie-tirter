"""

测试目标
1. 访问模式对文件的影响
2. 访问模式对write()的影响
3. 访问模式是否可以省略

"""

# r: 如文件不存在, 则报错；不支持写入操作, 表示只读
f = open("1.py", "r")
# f = open("文件操控实验1.txt", "r")  # 报错
# f.write("aa")  # 报错
f.close()

# w: 只写, 文件不存在, 新建文件;执行写入,会覆盖原有内容
f = open("1.py", "w")
f.write("a=b=3")
f.close

# a:追加, 如果文件不存在, 新建文件;在原有内容基础上, 追加新内容
f = open("2.py", "a")
f.write("a=b=7")
f.close()

# 访问模式是否可以省略
f = open("1.py")
f.close
