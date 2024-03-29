# 起名的方式:  (?P<名字>正则)  (?P=名字)
import re

msg = "<html><h1>abc</h1></html>"

result = re.match(r"<(?P<name>\w+)><(?P<name2>\w+)>(.+)</(?P=name2)></(?P=name)>", msg)
print(result)
print(result.group(1))
print(result.group(2))
print(result.group(3))

"""
分组: ()  -----> result.group(1) 获取组中匹配的内容
        在分组的时候还可以使用  |  
        result = re.match(r"(\d{3}|\d{4})-(\d{8})$", phone)
        print(result)
    不需要引用分组的内容:
    result = re.match(r"<[0-9a-zA-Z]+>(.+)</[0-9a-zA-Z]+>$", msg)
    print(result)
    print(result.group(1))
引用分组匹配内容:
    1. number  \number 引用第number组的数据
        result = re.match(r"<([0-9a-zA-Z]+)>(.+)</\1>$", msg1)
        print(result)
        print(result.group(1))
        print(result.group(2))
    
    2. ?P=<名字>
        result = re.match(r"<(?P<name>\w+)><(?P<name2>\w+)>(.+)</(?P=name2)></(?P=name)>", msg)
        print(result)
        print(result.group(1))
        
    re模块:
    match
    search
    findall
    sub(正则表达式, "新内容", string)  替换
    split  result = re.split(r"[, :]","jave:90, python:95")  在字符串中搜索如果遇到:或者, 就分割
           将分割内容都保存到列表中了
"""


def func(temp):
    num = temp.group()
    num1 = int(num) + 1
    return str(num1)


result = re.sub(r"\d+", func, "jave:90, python:95")
print(result)

result = re.split(r"[, :]","jave:90, python:95")
print(result)
