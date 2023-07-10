# 拿到页面源代码
# 提取和解析数据
import requests
from lxml import etree
import time

url = "https://www.zbj.com/search/service/?l=0&kw&r=1"
resp = requests.get(url)
# print(resp.text)

# 解析
html = etree.HTML(resp.text)

# 拿到每一个服务商的div
divs = html.xpath("""//*[@id="__layout"]/div/div[3]/div/div[3]/div[4]/div[1]/div""")
for div in divs:  # 每一个服务商信息
    price = div.xpath("./div[3]/div[1]/span/text()")[0].strip("￥")
    title = div.xpath("./div[3]/a/text()")[0]
    shop_detail = div.xpath("./a/div[2]/div[1]/div/text()")[0]
    city = div.xpath("./div[2]/a/div[2]/div[3]/span[2]/text()")[0]

    time.sleep(1)
