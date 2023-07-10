mystr = "hello world and itcast and ithemima and Python"
# find():查找子符存在字符串哪，没有就为-1
print(mystr.find("and"))   # 12
print(mystr.find("and ", 15, 30))         # 23
print(mystr.find("ands "))       # 返回为-1不存在，ands这个字符不存在
# index():查找子符存在字符串哪，不存在就报错
print(mystr.index("and"))    # 12
print(mystr.index("and", 15, 30))   # 23
# count():查找子符在字符串中出现的次数
print(mystr.count("and"))    # 3
print(mystr.count("and", 15,30))    # 1
# print(mystr.count("ands")   # 0
# rfind():和find()功能相等，但是方向为右侧开始
# rindex():和index()功能相等，但是方向为右侧开始
print(mystr.rfind("and"))
print(mystr.rindex("and"))