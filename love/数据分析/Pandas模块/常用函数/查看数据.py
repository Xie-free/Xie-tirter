import pandas as pd


# df.head(n): 显示前n行数据,默认5行
# df.tail(n): 显示后n行数据,默认5行
# df.info(): 显示数据的信息、包括列名、数据类型、缺失值等
# df.describe(): 显示数据的基本统计信息、包括均值、方差、最大值、最小值等
# df.shape: 显示数据的行数和列数
data = [
    {"name": "Google", "likes": 25, "url": "https://www.google.com"},
    {"name": "Runoob", "likes": 30, "url": "https://www.runoob.com"},
    {"name": "Taobao", "likes": 35, "url": "https://www.taobao.com"}
]
df = pd.DataFrame(data)
# 显示前两行数据
print(df.head(2))
# 显示最后一行数据
print(df.tail(1))
# 显示数据信息
print(df.info())
# 显示数据的行数和列数
print(df.shape)