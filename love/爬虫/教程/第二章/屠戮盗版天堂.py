# 1. 定位到2022必看片
# 2. 从2022必看片中提取到子页面的链接地址
# 3. 请求子页面的链接地址. 拿到我们想要的下载地址....
import requests
import re

domain = "https://www.dy2018.com/"
resp = requests.get(domain, verify=False)  # verify=False 去掉安全验证
resp.encoding = "gb2312"  # 指定编码方式
# print(resp.text)

# 拿到ul里面的li
obj1 = re.compile(r"2022必看热片.*?<ul>(?P<ul>.*?)</ul>", re.S)
obj2 = re.compile(r"<a href='(?P<href>.*?)'")
obj3 = re.compile(r"""◎片　　名(?P<moving>.*?)<br />.*?<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href=(?P<install>.*?)">""", re.S)

result = obj1.finditer(resp.text)
child_href_list = []
for i in result:
    ul = i.group("ul")

    # 提取子页面链接:
    result2 = obj2.finditer(ul)
    for it in result2:
        url = it.group("href")
        # 拼接子页面的url地址: 域名 + 子页面地址
        child_href = domain + url.strip("/")
        # print(child_href)
        child_href_list.append(child_href)  # 把子页面链接保存到列表里

# 提取子页面
for href in child_href_list:
    href_resp = requests.get(href, verify=False)
    href_resp.encoding = "gb2312"
    result3 = obj3.search(href_resp.text)
    print(result3.group("moving"))
    print(result3.group("install"))



