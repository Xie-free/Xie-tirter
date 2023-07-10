import pandas as pd  # 导入库,并取名为pd

# loc--通过自定义索引获取数据
data = [["China", 1328474], ["USA", 302841], ["Japan", 127953], ["India", 1151751]]  # 创建列表
df = pd.DataFrame(data, index=['a', 'b', 'c', 'd'], columns=["Country", "Population(thousands)"])  # 指定index
print(df)
print("\n")
# print(df.loc['a'])  # 打印'a'列所有元素,等价于下面一行代码
# print(df.loc['a', :])  # 打印'a'列所有元素
# print(df.loc[:, "Country"])  # 打印Country列
# print(df.loc["a":"c", "Country"])  # 打印a到c行的Country列
# df.loc["c", "Country"] = "None"  # 将c行的Country列修改成None
# print(df)

# iloc--通过数字索引获取数据
# iloc使用方法和loc基本一致,只不过iloc通过数字索引
# print(df.iloc[2, 1])  # 第2行第1列的数据(行和列都是从零开始数起)

# ix---loc和iloc的结合  !!! 从pandas1.0.0版本开始已经移除了ix方法
# ix是loc和iloc的结合, 可以混用数字和自定的标签进行索引
# print(df.ix["c", 1])  # 打印c行1列的数据(从0开始数起)
# print(df.ix[2, "Population(thousands)"])  # 打印第二行Population(thousands)列的数据(从0数起)

# Boolean索引
df_2 = df["Population(thousands)"] > 1000000  # 判断是否大于
print(df_2)
print("\n")
df_3 = df[df["Population(thousands)"] > 1000000]  # 大于该数值的数
print(df_3)
