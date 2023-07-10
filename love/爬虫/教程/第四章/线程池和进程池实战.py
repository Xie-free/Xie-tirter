# 1. 如何提取单个页面的数据
# 2. 上线程池, 多个页面同时抓取
import time

import requests
from lxml import etree
import csv
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

f = open("data.csv", mode="w", encoding="utf-8")
csv_write = csv.writer(f)

n = 1


def download_one_page(url):
    global n
    resp = requests.post(url, data={
        "current": n
    })
    n += 1
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
        # list_vegetables = prod_name + prod_cat + low_price + high_price + avg_price + place + unit_info + pub_date"
        # print(list_vegetables)
        # csv_write.writerow(list_vegetables)
        list_vegetables = [prod_name, prod_cat, low_price, high_price, avg_price, place, unit_info]
        csv_write.writerow(list_vegetables)


if __name__ == '__main__':
    # for i in range(10):  # 效率极其低下
    # download_one_page("http://www.xinfadi.com.cn/getPriceData.html")

    with ThreadPoolExecutor(50) as t:
        for i in range(1, 200):
            t.submit(download_one_page("http://www.xinfadi.com.cn/getPriceData.html"))

    print(f"{i}页完毕")
f.close()