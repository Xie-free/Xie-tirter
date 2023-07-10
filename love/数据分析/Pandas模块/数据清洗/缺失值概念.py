import pandas as pd

data = [["China", 1328474], ["USA", 302841], [None, None], ["India", None]]
df = pd.DataFrame(data, columns=["Country", "Population(thousands)"])
df.to_csv(r"C:\Users\Administrator\Desktop\data_csv.txt")
df_1 = pd.read_csv(r"C:\Users\Administrator\Desktop\data_csv.txt")
print(df_1.count())
print("\n")
df_2 = pd.read_csv(r"C:\Users\Administrator\Desktop\data_csv.txt", index_col=0)
print(df_2.isnull())  # 查看数据是否是缺失值
print("\n")
print(df_2.notnull())  # notnull()函数与之对应

df_3 = df_2.fillna("Done")  # 填充缺失值
print(df_3)

df_4 = df_2.dropna()  # 直接删除缺失值
print(df_4)