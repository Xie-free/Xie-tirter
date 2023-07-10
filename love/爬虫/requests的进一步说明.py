# 1.get请求和post请求
import requests

resp = requests.get("http://www.baidu.com/index.html")
print(resp.status_code)  # 返回状态码
print(resp.headers)  # 返回头部信息
print(resp.cookies)  #
