# qq = input("输入QQ号码:")
# if 5 <= len(qq) <= 13 and qq[0] != "0":
#     print("合法的")
# else:
#     print("不合法")

import re

msg = "娜扎热巴代斯丁真"
pattern = re.compile("丁真")

result = pattern.match(msg)  # 没有匹配
print(result)

# 使用正则re模块方法:  match

s = "娜扎热巴代斯丁真"

result = re.match("丁真", s)  # 只要从开头进行匹配, 如果匹配不成功则返回None
print(result)

result = re.search("丁真", s)  # search 进行正则字符串匹配的方法, 匹配的是整个字符串
print(result)

print(result.span())

print(result.group())  # 使用group提取匹配到的内容
print(result.groups())

# a2b h6k

s = "哈哈3a"

result = re.search("[0-9][a-z]", s)
print(result)

msg = "abcd7yjkfd8jas342h54d6k7f00"

result = re.search("[a-z][0-9][a-z]", msg)  # search只要有匹配的后面就不会继续进行检索, 找到一个匹配的就会停止

print(result.group())

result = re.findall("[a-z][0-9][a-z]", msg)  # findall 匹配整个字符串, 找到一个继续向下找一直到字符串结尾
print(result)
# 正则符号

# a7a a88a a7878a
msg = "a7aopa88akigka7878a"
result = re.findall("[a-z][0-9]+[a-z]", msg)
print(result)

# qq号码验证 5-11  开头不能是0
qq = "45345456"
result = re.match("^[1-9][0-9]{4,10}$", qq)
print(result)

# 用户名可以是字母或者数字, 不能是数字开头, 用户名必须6位以上 [0-9a-zA-Z]
user_name = "xie_520"
result = re.match("[a-zA-z][\w]{5,}$", user_name)
print(result)

msg = "aa.py ab.txt bb.py kk.png uu.py apyb.txt"
result = re.findall(r"\w+\.py\b", msg)
print(result)

'''
总结:
    任意字符除(\n)
    ^开头
    $结尾
    [] 范围  [abc] [a-z] [a0z*$&]    
    
    正则预定义:
    \s  空白 (空格)
    \b  边界
    \d  数字
    \w  word  [0-9a-zA-Z_]
    
    大写反面  \S  非空格  \D  非数字 .....
    
    "\w [0-9]"  ---->  \w [0-9] 只能匹配一个字母
    
    量词:
    * >=0
    + >=1
    ? 0,1
    
    手机号码正则
    re.match("1[35789]\d{9}$", phone)
    {m}:  固定m位
    {m,}: >m
    {m,n} phone >= m  phone<n
    


'''
