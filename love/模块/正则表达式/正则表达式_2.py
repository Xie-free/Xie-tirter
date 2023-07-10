# 分组
# 匹配数字 0-100 数字
import re

n = "98"

# 改进版
result = re.match("[1-9]?\d?$|100$", n)
print(result)

# (word|word|word)  区别   [abc]  表示的是一个字母而不是单词
# 验证输入的邮箱 163 126 qq
email_1 = "1123123123@qq.com"
result = re.match(r"\w{5,20}@(163|qq|126)\.(com|cn)", email_1)
print(result)

# 不是以4, 7结尾的手机号码(11位)

phone = "15901010889"
result = re.match(r"1\d{9}[0-35689]$", phone)
print(result)

# 爬虫
phone = "010-12345678"

result = re.match(r"(\d{3}|\d{4})-(\d{8})$", phone)
print(result)

# 分别提取
print(result.group())
# () 表示分组  group(1) 表示提取到第一组的内容  group(2)表示第二组的内容
print(result.group(1))
print(result.group(2))

#
msg = "<html>abc</html>"
msg1 = "<h1>hello</h1>"

result = re.match(r"<[0-9a-zA-Z]+>(.+)</[0-9a-zA-Z]+>$", msg)
print(result)
print(result.group(1))

# number
result = re.match(r"<([0-9a-zA-Z]+)>(.+)</\1>$", msg1)
print(result)
print(result.group(1))
print(result.group(2))

#
msg = "<html><h1>abc</h1></html>"

result = re.match(r"<([0-9a-zA-Z]+)><([0-9a-zA-Z]+)>(.+)</\2></\1>$", msg)
print(result)

print(result.group(1))
print(result.group(2))
print(result.group(3))