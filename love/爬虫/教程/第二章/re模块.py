import re

# # findall: 匹配字符串中所有符合正则得内容
# lst = re.findall(r"\d+", "我的电话是10051, 我朋友的电话是10081")
# print(lst)
#
# # finditer: 匹配字符串中所有的内容[返回的是迭代器], 从迭代器中拿到内容需要.group()
# it = re.finditer(r"\d+", "我的电话是10051, 我朋友的电话是10081")
# for i in it:
#     print(i.group())
#
# # search, 找到一个结果就返回，返回的对象是match对象. 那数据需要.group()
# s = re.search(r"\d+", "我的电话是10051, 我朋友的电话是10081")
# print(s.group())

# # match是从头开始匹配
# d = re.match(r"\d+", "我的电话是10051, 我朋友的电话是10081")
# print(d)
#
# # 预加载正则表达式
# obj = re.compile(r"\d+")
#
# a = obj.finditer("我的电话号码是100087,我朋友的电话号码是10010")
# for a in a:
#     print(a.group())
#
# b = obj.findall("0000089123离开教室的咯技术的老咔叽")
# print(b)


s = """
<div class='like'><span id='1'>中国联通</span></div>
<div class='yuu'><span id='2'>中国电信</span></div>
<div class='xie'><span id='3'>中国移动</span></div>
<div class='tory'><span id='4'>中国</span></div>
"""

# (?P<分组名字>正则) 可以单独从正则匹配的内容中进一步提取内容
obj = re.compile(r"<div class='.*?'><span id='(?P<id>\d+)'>(?P<name>.*?)</span></div>", re.S)  # re.S: 让.能匹配换行符

result = obj.finditer(s)
for i in result:
    print(i.group("name"))
    print(i.group("id"))


