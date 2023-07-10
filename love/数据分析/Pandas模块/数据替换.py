import pandas as pd
import numpy as np

data = pd.Series([1, -999, 2, -999, -1000, 3])
# print(data)

# data = data.replace(-999, np.nan)  # 替换为空值
# print(data)

# data = data.replace([-999, -1000], np.nan)  # 多个数替换为空值
# print(data)

# data.replace([-999, -1000], [np.nan, 0], inplace=True)  # 多个数据替换为多个数据,指定inplace对源数据进行修改
# print(data)

# data = data.replace({-999: np.nan, -1000: 0})  # 多个数据替换为多个数据
# print(data)

df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [1, 3, 5, 7, 9], 'C': ['a', 'b', 'c', 'd', 'e']})
# print(df)
# df.replace(5, 0, inplace=True)  # 将5替换成0,指定inplace参数为True

# 替换多个值也跟Series中一样,既可以用列表,也可以用字典
df.replace([1, 5], [5, 1], inplace=True)
print(df)