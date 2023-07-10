# find: 从左往右查找,只要遇到一个符合要求的则返回位置
# rfind:与find查找方向相反
# count: 统计指定字符串

path = "https://www.baidu.com/img/dong_asdfasdflkjaouiotqwetwqsd.jpg"
i = path.find(".")
item = path.rfind(".")
zhui = path[i:]
zhui = path[item+1:]

print(i)
print(zhui)
print(item)