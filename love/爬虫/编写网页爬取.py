import sys
import multiprocessing
import re
import os
import urllib.request as lib


def craw_links(url, depth, keywords, processed):
    """
    :param url: 抓取的网址
    :param depth: 要爬取的深度
    :param keywords: 要关注的关键字元组
    :param processed: 进程池
    :return:
    """
    contents = []
    # 检查URL是否以http://开头过或者以https://开头
    if url.startswith(("http://", "https://")):
        if url not in processed:
            # 将此URL标记为已处理
            processed.append(url)
        else:
            # 避免再次处理同一个URL
            return
        print('Crawing ' + url + '...')
        fp = lib.urlopen(url)
        # python3返回的是字节, 所以需要解码处理
        contents = fp.read()
        contents_decoded = contents.decode("UTF-8")  # 解码
        fp.close()
        pattern = "|".join(keywords)  # 定义正则的规则
        # 如果此页包含某些关键字,则将其保存到文件中
        flag = False
        if pattern:
            searched = re.search(pattern, contents_decoded)  # 匹配网页内容
        else:
            # 如果没有给出过滤关键字, 请保存当前页面
            flag = True
        if flag or searched:
            with open("craw\\" + url.replace(":", "_").replace("/", "_")+".text", "wb") as fp:
                fp.write(contents)
        # 查找当前页面中所有的连接
        links = re.findall("href='(.*?)'", contents_decoded)
        # 当前网页中所有的连接
        for link in links:
            # 考虑相对路径
            if not link.startswith(("http://", "https://")):
                try:
                    index = url.rindex("/")
                    link = url[0:index + 1] + link
                except:
                    pass
            if depth > 0 and link.endswith((".htm", ".html")):
                craw_links(link, depth - 1, keywords, processed)


if __name__ == '__main__':
    processed = []
    keywords = ("datetime", "KeyWord2")
    if not os.path.exists("craw") or not os.path.isdir("craw"):
        os.mkdir("craw")
    craw_links(r"http://www.baidu.com", 10, keywords, processed)
