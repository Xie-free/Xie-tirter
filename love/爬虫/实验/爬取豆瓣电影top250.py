from bs4 import BeautifulSoup  # 数据获取
import sys
import re  # 正则表达式-进行文字匹配
import urllib.request, urllib.error  # 指定URL,获取网页数据
import xlwt  # 进行excel的操作的
import sqlite3  # 进行数据库操作


def result():
    baseurl = "https://movie.douban.com/top250?start=0"
    # 1.爬取网页
    data_list = get_data(baseurl)
    # 2.解析数据
    # 3.保存数据
    save_path = r"F:\Python\love\爬虫\爬取数据文件\豆瓣电影top250.xls"
    save_data(data_list, save_path)


# 爬取网页
def get_data(baseurl):
    # 影片详情的规则
    find_link = re.compile(r'<a href="(.*?)">')  # 定义影片链接得正则规则
    # re.S让换行包含在字符中
    find_img = re.compile(r'<img .*? src="(.*?)"', re.S)  # 定义影片图片的正则规则
    # 影片片名
    find_title = re.compile(r'<span class="title">(.*?)</span>')  # 定义影片片名的正则规则
    # 影片评分
    find_rating = re.compile(r'<span class="rating_num".*?>(.*?)</')  # 定义影片评分的正则规则
    # 评价人数
    find_people = re.compile(r'<span>(.*?)人评价</span>')  # 定义影片人数的正则规则
    # 概况
    find_inq = re.compile(r'<span class="inq">(.*?)</')  # 定义影片概况的正则规则
    # 影片相关内容
    find_bd = re.compile(r'<p class="">(.*?)</p>', re.S)

    data_list = []
    for i in range(0, 10):  # 调用获取页面信息的函数
        url = baseurl + str(i * 25)
        html = get_url(url)  # 保存获取到的网页源码
        # 2.逐一解析数据
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all("div", class_="item"):  # 查找符合要求的字符串,形成列表
            # print(item)  # 查看是否运行成功
            data = []  # 保存一部电影的所有信息
            item = str(item)  # 转成字符串
            # 影片详情连接
            link = re.findall(find_link, item)[0]  # 获得影片链接
            data.append(link)
            img = re.findall(find_img, item)[0]  # 获得影片图片
            data.append(img)
            title = re.findall(find_title, item)  # 获得影片名字
            if len(title) == 2:  # 判断是否有两个名字
                c_title = title[0]  # 中文名
                data.append(c_title)
                e_title = title[1].replace("/", "")  # 去掉无关的符号
                data.append(e_title)  # 添加外国名
            else:
                data.append(title[0])  # 直接添加
                data.append(" ")  # # 如果只有一个,外国名要留空
            rating = re.findall(find_rating, item)[0]  # 获得影片评分
            data.append(rating)
            people = re.findall(find_people, item)[0]  # 获得评价人数
            data.append(people)
            inq = re.findall(find_inq, item)  # 获得影片概括
            if len(inq) != 0:
                data.append(inq[0].replace("。", ""))  # 去掉句号
            else:
                data.append(" ")
            bd = re.findall(find_bd, item)[0]  # 获得影片相关内容
            bd = re.sub("<br(\s+)?/>(\s+)?", " ", bd)  # 去掉<br/>
            data.append(bd.strip())
            data_list.append(data)  # 处理好的一部信息放在列表里
    print(data_list)
    return data_list


# 得到指定一个URL的网页内容
def get_url(url):
    head = {"User-Agent":  # 模拟浏览器头部信息,向豆瓣服务器发送消息
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ""Chrome/110.0.0.0 Safari/537.36"
            }
    # 用户代理:表示告诉豆瓣服务器,我们是什么类型的机器.
    # 浏览器(本质上是告诉浏览器,我们可以接受什么水平的内容)
    request_url = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request_url, timeout=5)
        html = response.read().decode("utf-8")
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        elif hasattr(e, "reason"):
            print(e.reason)
    return html


# 保存数据
def save_data(data_list, save_path):
    work_book = xlwt.Workbook(encoding="utf-8", style_compression=0)  # 创建work_book对象
    work_sheet = work_book.add_sheet("豆瓣电影top250", cell_overwrite_ok=True)  # 创建豆瓣电影top250这个sheet工作表
    col = ("电影详情链接", "电影图片链接", "影片原名",
           "影片翻译名", "评分", "评价人数", "概况", "相关信息")
    for i in range(0, len(col)):
        work_sheet.write(0, i, col[i])  # 表格的列名
    for content in range(0, len(data_list)):
        print(f"第{content}条")  # 打印执行第几条了
        data = data_list[content]
        for j in range(0, len(data)):
            work_sheet.write(content + 1, j, data[j])  # 数据内容
    else:
        work_book.save(save_path)  # 保存数据


if __name__ == '__main__':
    result()
    print("爬取完毕")
