# 登录 --> 得到cookie
# 带着cookie 去请求到书架url --> 书架上的内容

# 必须得把上面得两个操作连起来
# 我们可以使用session进行请求 --> session你可以认为是一连串的请求. 在这个过程中的cookie不会丢失
import requests
#
# # 会话
# session_ = requests.session()
# data = {"loginName": "15721388622",
#         "password": "mamingy.2020"}
#
# # 1. 登录
# url = "https://passport.17k.com/ck/user/login"
# result = session_.post(url, data=data)
# # print(result.text)
# # print(result.cookies)
#
# # 2. 拿书架上的书架
# # 刚才的那个session中是有cookie的
# resp = session_.get("https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919")
# print(resp.json())

resp = requests.get("https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919", headers={
        "Cookie": "GUID=786a3de1-6f88-45e7-89bd-f3eea4d5a0ca; sajssdk_2015_cross_new_user=1; c_channel=0; c_csc=web; accessToken=avatarUrl%3Dhttps%253A%252F%252Fcdn.static.17k.com%252Fuser%252Favatar%252F05%252F05%252F75%252F97767505.jpg-88x88%253Fv%253D1660115395000%26id%3D97767505%26nickname%3D%25E4%25B8%2580%25E8%25BA%25AB%25E5%2589%2591%25E6%25B0%2594%25E8%258D%25A1%25E6%25B1%259F%25E6%25B9%2596%26e%3D1675669687%26s%3Df50400dbc8f0b861; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2297767505%22%2C%22%24device_id%22%3A%22182868a9a8e33e-0ed6918a3819d8-26021d51-2073600-182868a9a8f6a3%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%22786a3de1-6f88-45e7-89bd-f3eea4d5a0ca%22%7D; Hm_lvt_9793f42b498361373512340937deb2a0=1660114607,1660118564; Hm_lpvt_9793f42b498361373512340937deb2a0=1660118628"
})
print(resp.text)