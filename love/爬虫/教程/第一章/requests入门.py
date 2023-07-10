# 安装requests
# pip install requests
# 国内源
# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple requests

import requests
Search_content = input("请输入您要搜素的内容")

url = f"https://www.sogou.com/web?query={Search_content}"

url_headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}

result = requests.get(url, headers=url_headers)  # 处理一个小小的反爬
print(result)
print(result.text)  # 拿到页面源代码