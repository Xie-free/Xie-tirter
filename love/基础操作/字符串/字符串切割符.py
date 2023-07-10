# replace(a,b,c):等同于把a替换成b，替换次数为c,c如果不填则为把所有a替换成b
s = "asdfasdfasdfasd"
a = s.replace("a", "*")

print(a)

# split(a,b):等同于把字符串a去掉,b为替换几次,然后把字符串转换列表
b = s.split("s")
print(b)

d = """sdfasdfasdfasd
sdfasdfasdfasddfasdfa
sdfasdfasdfasdasdfasdfasgasd
"""

# splitlines 等同于把字符串整理在一行里
print(d)
c = d.splitlines()
print(c)

e = "asdfasdfasdfasd"

f = e.partition(" ")
print(f)