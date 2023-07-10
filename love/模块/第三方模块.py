# 第三方:  pillow
# import pillow   pip install
import requests

response = requests.get("https://www.12306.cn/")
print(response.text)



