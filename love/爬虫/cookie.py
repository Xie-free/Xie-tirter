# 获取cookie

import requests

response = requests.get("http://www.baidu.com")
print(response.cookies)  # 打印cookies
print(type(response.cookies))  # 打印cookies的类型
for k, v in response.cookies.items():  # 从获取键值对的方式输出cookies的相应值
    print(k + ":", v)