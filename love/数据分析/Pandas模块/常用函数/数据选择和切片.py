import pandas as pd

# df[column_name]: 选择指定的列
# df.loc[row_index, column_name]: 通过标签选择数据
# df.iloc[row_index, column_index]: 通过位置选择数据
# df.ix[row_index, column_name]: 通过标签或位置选择数据
# df.filter(items=[column_name1, column_name2]): 选择指定的列
# df.filter(regex="regex"): 选择列名匹配正则表达式的列
# df.sample(n): 随机选择n行数据