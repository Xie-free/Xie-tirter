import pandas as pd

df = pd.read_csv("nba.csv")
# to_string()用于返回DataFrame类型的数据
# 如果不使用该函数,则输出结果为前五行和后五行
# print(df.to_string())

# 我们也可以使用to_csv()方法将DataFrame存储为csv文件
nme = ["Google", "Runoob", "Taobao", "Wiki"]
st = ["www.google.com", "www.runoob.com", "www.taobao.com", "www.wikipedia.org"]
ag = [90, 40, 80, 98]

# 字典
dict_data = {"name": nme, "site": st, "age": ag}

df_1 = pd.DataFrame(dict_data)

# 保存dataframe
df_1.to_csv("site.csv")

# head()方法用于读取前面的n行,如果不填参数n, 默认返回5行
print(df.head())

# 读取前面10行
print(df.head(10))

# tail(n)方法用于读取尾部的n行, 如果不填参数n, 默认返回5行
print(df.tail())

# 读取后面10行
print(df.tail(10))

# info()返回表格的一些基本信息
print(df.info())
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 458 entries, 0 to 457          # 行数，458 行，第一行编号为 0
# Data columns (total 9 columns):            # 列数，9列
#  #   Column    Non-Null Count  Dtype       # 各列的数据类型
# ---  ------    --------------  -----
#  0   Name      457 non-null    object
#  1   Team      457 non-null    object
#  2   Number    457 non-null    float64
#  3   Position  457 non-null    object
#  4   Age       457 non-null    float64
#  5   Height    457 non-null    object
#  6   Weight    457 non-null    float64
#  7   College   373 non-null    object         # non-null，意思为非空的数据
#  8   Salary    446 non-null    float64
# dtypes: float64(4), object(5)                 # 类型
# 写入文件时,当参数为空值时,需要设置to_csv()函数的na_rap参数修改为NULL
# 如果存在空值就保存为NULL
data = [
    {
        "a": 1, "b": 2, "c": 10
    },
    {
        "a": 5, "b": 10, "c": 12
    }
]
df_2 = pd.DataFrame(data)
print(df_2.to_string())
# df_2.to_csv("test.csv")  # 此时空值为空
# df_2.to_csv("test_new.csv", na_rep="NULL")  # 此时空值为NULL
