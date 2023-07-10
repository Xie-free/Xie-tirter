# replace: 将子符修改
a = "hell world and itcast and ithemima and Python"
b = a.replace("and", "he")
print(a)
print(b)
# split:把子符改成修改号，比如and修改成,
c = a.split("and")
d = a.split("and", 2)
print(c)
print(d)
# join:把子符合并
mylist = ["aa", "bb", "cc"]
x = "".join(mylist)
print(x)
# capitalize:将字符串第一个字符转换成大写,只有首大写
print(a.capitalize())
# title:将字符串每个单词首字母转换成大写
print(a.title())
# lower:将字符串中大写转换小写
print(a.lower())
# upper:将字符串中小写转换成大写
print(a.upper())
