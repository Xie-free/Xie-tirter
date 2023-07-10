# 安装
# pip install bs4 -i 清华
import requests
from bs4 import BeautifulSoup
import csv


f = open("菜价.csv", mode="wb")
csv_write = csv.writer(f)
# 页面源代码
url = "http://www.xinfadi.com.cn/priceDetail.html"
# 页面使用了服务器渲染, 所以有个菜名html
food_url = "http://www.xinfadi.com.cn/getPriceData.html"
resp = requests.post(food_url)
result = resp.json()
food_list = result["list"]
# print(food_list)
for i in food_list:
    prod_name = i["prodName"]
    prod_cat = i["prodCat"]
    low_price = i["lowPrice"]
    high_price = i["highPrice"]
    avg_price = i["avgPrice"]
    place = i["place"]
    unit_info = i["unitInfo"]
    pub_date = i["pubDate"]
    print([prod_name, prod_cat, low_price, high_price, avg_price, place, unit_info, pub_date])

# f.close()

# food_list = result["list"]
# print(food_list)





# 解析数据
# 1. 把菜名源代码交给BeautifulSoup进行处理
# page = BeautifulSoup(resp.text,  "html.parser")  # 指定html解析器
# 2. 从bs对象中查找数据
# find(标签, 属性=值)  只找第一个
# find_all(标签, 属性=值)  返回全部
# 如class是python里面的关键字, 可以在属性后面加_
# table = page.find("table", class_="hq_table") # class 是python里的关键字
# table = page.find("table", attrs = {"class": "hq_table"}) # 和上一行是一个意思,可以避免关键字
# 拿到所有数据行
# trs = table.find_all("tr")[1:]  从第一个开始,把开头的tr干掉不用
# for tr in trs:  # 每一行
    # tds = tr.find_all("td")  # 拿到每行中的所有td
    # name = tds[0].text  # .text 表示拿到被标签标记的内容
    # low = tds[1].text
    # avg = tds[2].text
    # high = tds[3].text
    # gui = tds[4].text
    # kind = tds[5].text
    # date = tds[6].text
    # print(name, low, avg, high, gui, kind, date)
    # csv_writer.writerow(name, low, avg, high, gui, kind, date)
# f.close()
# print("over")