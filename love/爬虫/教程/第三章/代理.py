# 原理: 通过第三方的一个机器人去发送请求
import requests

proxies = {
    "https": "https://(ip地址)"
}
resp = requests.get("http://www.baidu.com")
# resp = requests.get("http://www.baidu.com", proxies=proxies)
resp.encoding = "utf-8"
print(resp.text)
