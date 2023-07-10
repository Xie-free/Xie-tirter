from urllib.parse import urlparse, urljoin, urlsplit

o = urlparse("http://www.baidu.com")
print(o.port)

print(o.hostname)

print(urljoin("http://www.baidu.com", "index.html"))  # 拼接url

url = r"https://www.baidu.com"
r1 = urlsplit(url)
print(r1.hostname)

print(r1.geturl())  # https://www.baidu.com

print(r1.netloc)  # www.baidu.com

print(r1.scheme)  # https