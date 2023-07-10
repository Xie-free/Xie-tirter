import re

# 默认是贪婪的, 如果想将贪婪模式变成非贪婪模式
msg = "abc123abc"

result = re.match(r"abc(\d+?)", msg)
print(result)

path = "https://iwtf1.caching.ovh/to/that/2020/09/26/aaa000197b8a1006cec2d2d.jpg"
website = re.match(r"(.*)",path)
print(website.group(1))
website = website.group(1)
import requests

response = requests.get(website)

with open("aa.jpg", "wb") as w_stream:
    w_stream.write(response.content)
