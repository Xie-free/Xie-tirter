import pandas as pd  # 导入模块,取名为pd

data = [["China", 1328474], ["USA", 302841], [None, None], ["India", 1151751]]  # 创建列表
df = pd.DataFrame(data, index=['a', 'b', 'c', 'd'], columns=["Country", "Population(thousands)"])  # 指定index
# df.to_csv(r"C:\Users\Administrator\Desktop\data_csv.txt")  # 保存到桌面,文件为:data_csv
df.to_csv(r"C:\Users\Administrator\Desktop\data_csv.txt", sep="\t", na_rep="NULL")  # 将分隔符改成制表符,将空置替换成NULL
# df.to_csv(r"C:\Users\Administrator\Desktop\data_csv.txt", header=None, index=None)  # 不保存列标签和行标签 df_read =
# pd.read_csv(r"C:\Users\Administrator\Desktop\data_csv.txt")  # 读取data_csv里的数据(默认分隔符为(,)逗号) print(df_read) df_read_1
# = pd.read_table(r"C:\Users\Administrator\Desktop\data_csv.txt")  # 读取data_csv文件里的数据(默认分隔符为(\t制表符),将其设置为(,
# )逗号) print(df_read_1) df_1 = pd.read_table(r"C:\Users\Administrator\Desktop\data_csv.txt",index_col=0)  # 指定第0列是行标签
# print(df_1)

df_1 = pd.read_table(r"C:\Users\Administrator\Desktop\data_csv.txt", names=["Cou", "Pop"])  # 设置标签
print(df_1)
