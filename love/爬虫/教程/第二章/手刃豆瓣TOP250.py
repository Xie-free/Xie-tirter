# 拿到页面源代码.    requests
# 通过re来提取想要的有效信息  re
import requests
import re
import csv

url = "https://movie.douban.com/top250"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}
resp = requests.get(url, headers=headers)
page_content = (resp.text)

# 解析数据
obj_name = re.compile(r"""<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)</span>.*?<p class="">.*?<br>(?P<year>.*?)&nbsp.*?<span class="rating_num" property="v:average">(?P<score>.*?)</span>.*?<span>(?P<people>.*?)</span>""", re.S)
# 开始匹配
result = obj_name.finditer(page_content)
f = open("data.csv", mode="w", encoding="utf-8")
csv_writer = csv.writer(f)
for i in result:
    # print(i.group("name"))
    # print(i.group("year").strip())
    # print(i.group("score"))
    # print(i.group("people"))
    dit = i.groupdict()  # 创造字典形式
    dit["year"] = dit["year"].strip()
    csv_writer.writerow(dit.values())

f.close()
resp.close()
print("over")