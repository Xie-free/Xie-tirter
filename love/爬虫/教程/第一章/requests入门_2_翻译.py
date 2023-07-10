# import requests
# import re
#
# url = "https://fanyi.baidu.com/sug"
# phrases_url = "https://fanyi.baidu.com/v2transapi?from=en&to=zh"
#
# name = ["editor", "effect", "educate", "effort", "eggplant", "elder", "elect", "electric",
#         "electrical", "electricity", "electronic", "element", "else", "e-mail",
#         "emergency", "emotion", "emphasize", "employ", "empty", "encourage",
#         "end", "enemy", "energetic", "energy", "engage", "engine", "engineer",
#         "England", "English", "enquiry", "enroll", "ensure", "enterprise",
#         "entertain", "entertainment", "entire", "entrance", "entry", "envelope", "environment", "equal", "eager"]
# E_2 = "enjoy enquiry enroll enter entertain envelope environment equal equality equip eraser escape especially establish estimate Europe even event eventually ever evidence exact examination example examine except exchange excite executive exercise exhibition exist existence exit expand expect expense" \
#       " expensive experience experiment expert expire explain explode expose export extra extremely eyesight"
# F_1 = "face factor factory fail failure fair fairly faith false fame familiar family famous fancy fan fantastic fantasy" \
#       " fare farewell fashion fasten fault favour favourite fax fear feather February federal" \
#       " fee feed feedback feel fellow female fence ferry festival fetch fever few field fierce fight figure file" \
#       " fill final finance find fine finger firefighter fireworks firm fisherman fit fist"
# # phrases_1 = "get along with  keep one's promise  easy-going  quarrels and fight" \
# #             "  have a good sense of humor  complain to sb  be strict with sb  look forward to sth doing sth"
#
# # xiu = phrases_1.replace("  ", ",")
# # letter_list = phrases_1.split("  ")
# print(letter_list)
# num = len(letter_list)
# a = 0
# for i in letter_list:
#     translate = i
#
#     dat = {
#         "kw": translate
#     }
#
#     # 发送post请求, 发送的数据必须在字典中, 通过data参数进行传递
#     resp = requests.post(url=url, data=dat)
#     result = resp.json()  # 将服务器返回的内容直接处理成json()  ---> dict
#     # print(result)
#     data = result["data"]
#     # print(data)
#     for it in data:
#         # print(it)
#         e_name = it["k"]
#         e_explain = it["v"]
#         print(f"{e_name}:{e_explain}")
#         a += 1
#         break
# print(f"总计{num}, 搜索到{a}")
#
