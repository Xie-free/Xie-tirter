"""
ljust():返回一个原字符串左对齐，并使用指定字符（默认空格）填写至对应长度的新字符串
语法
1字符串序列。ljust(长度,填充字符）
"""
my_like = "谢容容"
live = my_like.ljust(10, ".")
print(live)

# rljust():右对齐
like = my_like.rjust(10, ".")

print(like)
# center():中心对齐
my = my_like.center(10, ".")
print(my)