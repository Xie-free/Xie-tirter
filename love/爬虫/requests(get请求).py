import requests

# r = requests.get(url="https://www.baidu.com")
# print(r.status_code)  # 打印状态码
# print(r.url)  # 打印请求url
# print(r.headers)  # 打印头信息
# print(r.cookies)  # 打印cookie信息
# print(r.text)  # 以文本形式打印网页源码
# print(r.content)  # 以字节流形式打印
# resp = requests.get("http://httpbin.org/get")
# print(resp.text)

# response = requests.get("http://httpbin.org/get?name=gemey&age=22")
# print(response.text)
#
# data = {
#     "name": "tom",
#     "age": 20
# }
#
# response_1 = requests.get("http://httpbin.org/get", params=data)
# print(response_1)

response = requests.get("http://httpbin.org/get")
# print(response.text)
print(response.json())  # 方法同json.loads(response.text)
print(type(response.json()))