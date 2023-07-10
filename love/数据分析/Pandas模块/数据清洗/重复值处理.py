import pandas as pd

data = [["China", 1328474], ["USA", 302841], ["Japan", 127953], ["India", 1151751]]  # 创建列表
df = pd.DataFrame(data, columns=["Country", "Population(thousands)"])  # 指定列
df.to_csv(r"C:\Users\Administrator\Desktop\data_csv.txt")  # 保存到桌面
df_r = pd.read_csv(r"C:\Users\Administrator\Desktop\data_csv.txt", index_col=0)  # 读取数据
# sort_values()进行排序
print(df_r.sort_values("Population(thousands)"))  # 先进行排序,如果相同的数据,排序之后的位置一定是相邻的
# duplicated()查看数据是否重,如果一条数据是第一次出现那么返回False,如果之前已经出现过了,那么再次出现的话则回返回True.
print(df_r.duplicated())
# drop_duplicates()可以直接删除重复的数据项,即在返回值为True的数据项
print(df_r.drop_duplicates)