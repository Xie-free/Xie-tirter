import urllib.request
import urllib.parse
import webbrowser

# fp = urllib.request.urlopen(r"http://www.python.org")
# print(fp.read(100))  # 读取字节
# print(fp.read(100).decode())
# fp.close

# data = urllib.parse.urlencode({"spam": 1, "eggs": 2, "bacon": 0})
# data = data.encode("ascii")
# with urllib.request.urlopen("http://www.hongyaa.com.cn", data) as f:
#     print(f.read().decode("utf-8"))

webbrowser.open("http://www.python.org")