"""
BeautifulSoup4将复杂HTML文档转成一个复杂的树形结构.
每个节点都是Python对象,所有对象可以归纳为4种:

- Tag
- NavigableString
- BeautifulSoup
- Comment
"""
import re

from bs4 import BeautifulSoup

file = open("./baidu.html", "rb")
html_1 = file.read()
bs = BeautifulSoup(html_1, "html.parser")

# print(bs.title)
# print(bs.a)
# print(bs.head)  # 标签和内容

# print(type(bs.head))

# 1.Tag 标签及其内容

# print(bs.title.string)  # 内容
# print(type(bs.title.string))

# NavigableString  标签里的内容(字符串)

# print(bs.a.attrs)  # 获取a标签里属性和属性的值,返回一个字典

# print(type(bs))

# 3. BeautifulSoup  表示整个文档

# print(bs.name)
# print(bs.attrs)
# print(bs)


# print(bs.a.string)
# print(type(bs.a.string))

# 4. Comment 是一个特殊的NavigableString  输出内容不包含注释符号

# 文档的遍历
# print(bs.head.contents)  # 获取content的所有内容,返回为列表
# print(bs.head.contents[1])
# 更多内容, 查询官方文档


# 文档的搜素

# find_all(): 查找所有
# 字符串过滤: 会查找与字符串完全匹配的内容
# t_list = bs.find_all("a")
# print(t_list)

# 正则表达式搜素: 使用search
# t_list = bs.find_all(re.compile("a"))
# print(t_list)

# 方法: 传入一个函数(方法), 根据函数的要求来搜素 (了解)
# def name_is_exists(tag):
#     return tag.has_attr("name")

# t_list = bs.find_all(name_is_exists)
# print(t_list)

# 2.kwargs 参数
# t_list = bs.find_all(id="head")
# t_list = bs.find_all(class_=True)
# t_list = bs.find_all(href="baidu.com")

# 3.text参数
# t_list = bs.find_all(text="新闻")
# t_list = bs.find_all(text=["新闻", "贴吧", "地图"])
# t_list = bs.find_all(text=re.compile("\d"))  应用正则表达式来查找包含特定文本的内容(标签里的字符串)
# for i in t_list:
#     print(i)

# 4.limit 参数

# t_list = bs.find_all("a", limit=3)  # 限定搜索个数

# css选择器

# t_list = bs.select("title")  # 通过标签来查找

# t_list = bs.select(".mnav")  # 通过类名来查找

# t_list = bs.select("#u1")  # 通过id来查找

# t_list = bs.select("a[class=''bri]")  # 通过属性查找

# t_list = bs.select("head > title")  # 通过子标签来查找

t_list = bs.select(".manv ~ .bri")
print(t_list[0].get_text())