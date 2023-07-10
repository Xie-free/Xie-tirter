import pandas as pd  # 导入模块

# 正常修改数据轴索引的方法
# df = pd.DataFrame({
#     "a": [1, 2, 3],
#     "b": [4, 5, 6]
# })
# print(df)
# df.columns = ["c", "b"]
# df.index = [1, 2, 3]
# print(df)

# 我们利用rename()函数,指定columns参数,通过字典方式来重命名列索引
# df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
# print(df)
# df.rename(columns={"A": "a", "B": "c"}, inplace=True)
# print(df)


# df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
# print(df)
# # str.lower表示转换为小写
# # str.upper表示转换为大写
# df.rename(str.lower, axis="columns", inplace=True)
# print(df)

# 上面两种方法介绍如何修改列索引
# 接下来将如何修改行索引,可以指定axis参数为index,表示为行索引
# df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
# print(df)
# df.rename({1: 2, 2: 4}, axis="index", inplace=True)
# print(df)

# reindex()函数, 调用reindex方法后,会根据新索引进行重新排序
index = ["Firefox", "Chrome", "Safari", "IE10", "Konqueror"]
df = pd.DataFrame({
    "http_status": [200, 200, 404, 404, 301],
    "response_time": [0.04, 0.02, 0.07, 0.08, 1.0]
}, index=index)
# print(df)
new_index = ["Safari", "Iceweasel", "Comode Dragon", "IE10", "Chrome"]
# df = df.reindex(new_index)
# 其中, 新标签中的lceweasel和Comodo Dragon在原有标签中不存在
# 所以它们所对应的数据部分是NaN空值
# print(df)
# 重新排列列标签也是同样的,还可以指定fill_value参数填充空数据.
print(df.reindex(columns=["http_status", "user_agent"], fill_value=0))
print(df.reindex(["http_status", "user_agent"], axis="columns", fill_value=0))


