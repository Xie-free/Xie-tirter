import urllib.request
import urllib.parse

# 获取一个get请求
# result = urllib.request.urlopen("http://www.baidu.com")
# print(result.read().decode("utf-8"))  # 对获取到的网页源码进行utf-8解码

# 获取一个post请求

# data = bytes(urllib.parse.urlencode({"hello": "world"}), encoding="utf-8")
# result = urllib.request.urlopen("http://httpbin.org/post", data=data)
# print(result.read().decode("utf-8"))

# 超时处理
# try:
#     result = urllib.request.urlopen("http://httpbin.org/get", timeout=1)  # 申请超时
#     print(result.read().decode("utf-8"))
# except urllib.error.URLError as e:
#     print("请求超时")

# result = urllib.request.urlopen("http://httpbin.org/get")
# print(result.status)  # 状态码
# print(result.getheaders())  # 请求的头部信息,所有信息
# print(result.getheader("Server"))  # 请求的头部信息,只获取Server对应的值


# url = "http://httpbin.com"
# headers = {
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
#
# }
# data = bytes(urllib.parse.urlencode({"name":"xie"}), encoding="utf-8")
# req = urllib.request.Request(url=url, data=data, headers=headers, method="POST")
# result = urllib.request.urlopen(req)
# print(result.read().decode("utf-8"))

url = "https://www.baidu.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"

}
req = urllib.request.Request(url=url,headers=headers)
result = urllib.request.urlopen(req)
print(result.read().decode("utf-8"))
