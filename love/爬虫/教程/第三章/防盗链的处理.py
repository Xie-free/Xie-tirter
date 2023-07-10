# 1. 拿到contId
# 2. 拿到videoStatus返回的json
# 3. srcURL里面的内容进行修整
# 4. 下载视频
import requests

# 拉起视频的地址
url = "https://www.pearvideo.com/video_1028779"
contId = url.split("_")[1]

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
    # 防盗链: 溯源, 当前本次请求的上一级是谁
    "Referer": url
}

video_Status = f"https://www.pearvideo.com/videoStatus.jsp?contId={contId}&mrd=0.19374911787876337"
resp = requests.get(video_Status, headers=headers)
result = resp.json()
srcUrl = result["videoInfo"]["videos"]["srcUrl"]
systemTime = result["systemTime"]
srcUrl = srcUrl.replace(systemTime, f"cont-{contId}")

with open("视频/a.ma4", mode="wb") as f:
    f.write(requests.get(srcUrl).content)
