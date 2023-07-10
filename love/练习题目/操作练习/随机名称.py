import random

s = "qqemrvxboizxuycoifygksjhahbzmcnvbbvretkiyuowqlwhzvmbuyrtoqcnmbvzsdfytoqiwetryjkfvgfsalf"
a = ""
number = 0



while number < 5:
    for i in range(6):
        b = random.randint(0, len(s) - 1)
        a += s[b]
        if len(a) == 6:
            print(a.capitalize())
            a = ""
            number += 1

