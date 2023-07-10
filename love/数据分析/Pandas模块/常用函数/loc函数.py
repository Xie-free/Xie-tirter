import pandas as pd

data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

# 数据载入到DataFrame对象
df = pd.DataFrame(data)

# 源数据形式
print(df)
print("*" * 50)
# 返回第一行, 返回结果其实就是一个Pandas Series数据
print(df.loc[0])
print("*" * 50)
# 返回第二行
print(df.loc[1])
print("*" * 50)
# 也可以返回多行数据[[....]]格式, ...为各行的索引,以逗号隔开
# 返回的是DataFrame数据
print(df.loc[[0, 1]])
print("*" * 50)

# 使用loc属性返回指定索引到对应的某一行
df_1 = pd.DataFrame(data, index=["day1", "day2", "day3"])
# 指定索引
print(df_1.loc["day2"])