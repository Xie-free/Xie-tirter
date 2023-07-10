"""

1. 用户输入目标文件
2. 规划备份文件的名字
2.1 提取后缀 -- 找到名字中的点 -- 名字和后缀分离 -- 最右侧的点才是后缀的点 -- 字符串查找某个子串  rfind
2.2 组织新名字 = 原名字 + [备份] + 后缀
2.21 原名字就是字符串中的一部分字子串 -- 切片[开始:结束:步长]
3. 备份文件写入数据(数据和原文件一样)
3.1 打开 原文件 和 备份文件
3.2 原文件读取, 备份文件写入
3.21 如果不确定目标文件大小, 循环读取写入, 当读取数据没有了终止循环
3.3 关闭文件

"""

# 1.
old_name = input("请输入您要备份文件名字：")

# 2.1
index = old_name.rfind(".")
# print(old_name[:index])
# print(old_name[index:])

# 4. 思考: 有效文件备份 .txt
if index > 0:
    # 提取后缀
    postfix = old_name[index:]

# 2.2
# new_name = old_name[:index] + "[备份]" + old_name[index:]
new_name = old_name[:index] + "[备份]" + postfix

# 3.1
old_f = open(old_name, "rb")
new_f = open(new_name, "wb")

# 3.2
while True:
    con = old_f.read(1024)
    if len(con) == 0:
        # 读取完成了, 终止循环
        break
    new_f.write(con)

# 3.3
old_f.close()
new_f.close()
