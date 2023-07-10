import pandas as pd

# Pandas 清洗空值
# 如果我们要删除包含空字段的行
# 可以使用dropna()方法
# df = pd.read_csv("property-data.csv")
# print(df["NUM_BEDROOMS"])
# print("*" * 50)

# # 我们可以通过isnull()判断每个单元格是否为空
# print(df["NUM_BEDROOMS"].isnull())  # 此时Pandas把n/a和NA当作空数据,
# # na不是空数据, 不符合我们的要求, 我们可以指定空数据类型

# 设置空值的格式 na_values
# missing_values = ["n/a", "na", "--"]
# df_1 = pd.read_csv("property-data.csv", na_values=missing_values)
# print(df_1["NUM_BEDROOMS"])
# print(df_1["NUM_BEDROOMS"].isnull())

# # 删除包含空数据的行
# df = pd.read_csv("property-data.csv")
# print(df.to_string())
# print("**" * 50)
# new_df = df.dropna()
# # 默认情况下, dropna()方法返回一个新的DataFrame, 不会修改源数据
# # 如果你要修改源数据DataFrame, 可以使用inplace = True 参数
# print(new_df.to_string())
# df_1 = pd.read_csv("property-data.csv")
# df_1.dropna(inplace=True)
# print(df_1.to_string())

# # 移除指定列有空值的行 subset
# df = pd.read_csv("property-data.csv")
# print(df.to_string())
# print("**" * 50)
# # 移除ST_NUM列中字段值为空的行
# df.dropna(subset=["ST_NUM"], inplace=True)
# print(df.to_string())

# # fillna()方法来替换一些空字段
# df = pd.read_csv("property-data.csv")
# print(df.to_string())
# print("**"*50)
# df.fillna(12345, inplace=True)
# print(df.to_string())

# 我们也可以指定某一个列来替换数据
# df = pd.read_csv("property-data.csv")
# df["PID"].fillna(12345, inplace=True)
# print(df.to_string())

# # 替换空单元格的常用方法是计算列的均值、中位数值或众数
# # Pandas使用:
# # mean()计算列的均值(所有值加起来的平均值)
# # median()中位数值(排序后排在中间的数)
# # mode()众数(出现频率最高的数)
# df = pd.read_csv("property-data.csv")
# x = df["ST_NUM"].mean()
# df["ST_NUM"].fillna(x, inplace=True)
# print(df.to_string())

# 清洗格式错误的数据
# 数据格式错误的单元格会使数据分析变得困难,甚至不可能.
# 我们可以通过包含单元格的行, 或者将列中的所有单元格转换为相同格式的数据
# # 第三个日期格式错误
# # 以下实例会格式化日期
# data = {
#     "Data": ["2020/12/01", "2020/12/02", "20201226"],
#     "duration": [50, 40, 45]
# }
# df = pd.DataFrame(data, index=["day1", "day2", "day3"])
# print(df.to_string())
# print("**" * 50)
# df["Data"] = pd.to_datetime(df["Data"])
# print(df.to_string())

# 数据错误也是很常见的情况, 我们可以对错误的数据进行替换或是移除.
# 以下实例会替换错误年龄的数据
# person = {
#     "name": ["Google", "Runoob", "Taobao"],
#     "age": [50, 40, 12345]  # 12345 年龄数据是错误的
# }
# df = pd.DataFrame(person)
# print(df.to_string())
# df.loc[2, "age"] = 30  # 修改数据
# print(df.to_string())

# # 也可以设置条件格式
# # 将age大于120的设置为120
# person = {
#     "name": ['Google', 'Runoob', 'Taobao'],
#     "age": [50, 200, 12345]
# }
# df = pd.DataFrame(person)
# for x in df.index:
#     if df.loc[x, "age"] > 120:
#         df.loc[x, "age"] = 120# print(df.to_string())

# # 也可以将错误数据的行删除
# # 将age大于120的删除
# person = {
#     "name": ['Google', 'Runoob', 'Taobao'],
#     "age": [50, 40, 12345]  # 12345 年龄数据是错误的
# }
# df = pd.DataFrame(person)
# for x in df.index:
#     if df.loc[x, "age"] > 120:
#         df.drop(x, inplace=True)
# print(df.to_string())

# Pandas 清洗重复数据
# 如果我们要清洗重复数据, 可以使用duplicated()和drop_duplicates()方法
# 如果对应的数据是重复的, duplicated()会返回True, 否则返回False.
# person = {
#   "name": ['Google', 'Runoob', 'Runoob', 'Taobao'],
#   "age": [50, 40, 40, 23]
# }
# df = pd.DataFrame(person)
# print(df.duplicated())

persons = {
  "name": ['Google', 'Runoob', 'Runoob', 'Taobao'],
  "age": [50, 40, 40, 23]
}
df = pd.DataFrame(persons)
df.drop_duplicates(inplace=True)
print(df)