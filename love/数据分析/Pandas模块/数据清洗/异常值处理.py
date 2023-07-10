import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10, 8))  # 创建对象,生成10行8列的随机数据
df.to_csv(r"C:\Users\Administrator\Desktop\data_csv.txt")  # 导出数据到csv文件存到桌面
df_r = pd.read_csv(r"C:\Users\Administrator\Desktop\data_csv.txt", index_col=0)  # 读取数据,指定其中第0列为索引
# print(df_r)  # 数据之间出现了省略号,因为DataFrame有默认显示长度,一旦超过这个值就会显示为省略号
# 为了解决,在set_option()函数中设置参数display.width为None即可
pd.set_option("display.width", None)  # 不限制显示宽度
# print(df_r)
# print(df_r.count())  # 打印非空值，默认参数为0,参数为0表示按列求值,参数为1表示按行求值

# 还可以使用sum()按各列求和, df.mean()按各列求平均值,df.median()求中位数.
# 函数默认参数为0,参数为0表示按列求值,参数为1表示按行求值.

# print(df_r.sum())  # 求和
# print(df_r.mean())  # 求平均值
# print(df_r.median())  # 求中位数

# 还可以使用var()求方差, std()求标准差, mad()根据平均值计算平均绝对利差.
# 函数默认参数为0,参数为0表示按列求值,参数为1表示按行求值.

# print(df_r.var())  # 求方差
# print(df_r.std())  # 求标准差
# print(df_r.mad())  # 平均绝对利差

# 还可以使用max()求最大值, min()求最小值.
# 函数默认参数为0,参数为0表示按列求值,参数为1表示按行求值.

# print(df_r.max())  # 求最大值
# print(df_r.min())  # 求最小值

# 使用describe()可以一次性完成上述多种功能
# 函数默认参数为0,参数为0表示按列求值,参数为1表示按行求值.

# print(df_r.describe())

# abs()可以对数据绝对值化, all()判断数据是否全部为真, any()判断是否存在真
# 函数默认参数为0,参数为0表示按列求值,参数为1表示按行求值.

# tem = df_r.abs() < 1  # 绝对值小于1的数据
# print(tem)
# print(tem.all())
# print(tem.any())

mea = df_r.mean()  # 获取平均值
df_a = df_r[df_r.abs() < 1]  # 绝对值小于1的数据
df_a = df_a.fillna(mea)  # 填充平均值
print(df_a)
