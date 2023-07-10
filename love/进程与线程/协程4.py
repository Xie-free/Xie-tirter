# 案例
import gevent
import requests
from gevent import monkey

monkey.patch_all()
import urllib.request


def down_load(url):
    response = urllib.request.urlopen(url)
    content = response.read()
    print(f"下载了{url}的数据,长度:{len(content)}")


if __name__ == '__main__':
    urls = ["http://www.163.com", "http://www.qq.com", "http://www.baidu.com"]
    g1 = gevent.spawn(down_load, urls[0])
    g2 = gevent.spawn(down_load, urls[1])
    g3 = gevent.spawn(down_load, urls[2])

    # gevent.joinall(g1, g2, g3)  # 类似 g1.join g2.join g3.join
    g1.join()
    g2.join()
    g3.join()