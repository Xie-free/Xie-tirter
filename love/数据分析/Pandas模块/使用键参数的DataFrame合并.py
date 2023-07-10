import pandas as pd

left = pd.DataFrame({"key1": ["k0", "k0", "k1", "k2"],
                     "key2": ["k0", "k1", "k0", "k1"],
                     "A": ["A0", "A1", "A2", "A3"],
                     "B": ["B0", "B1", "B2", "B3"]})

right = pd.DataFrame({"key1": ["k0", "k1", "k1", "k2"],
                      "key2": ["k0", "k0", "k0", "k0"],
                      "C": ["C0", "C1", "C2", "C3"],
                      "D": ["D0", "D1", "D2", "D3"]})

# result = pd.merge(left, right, on=["key1", "key2"])  # 连接键为key
# print(result)

# 将how参数设置为outer(使用两个帧中的键的并集)
result_1 = pd.merge(left, right, how="outer", on=["key1", "key2"])
print(result_1)
print("**" * 50)

# 将how参数设置为left, 表示仅使用左框架中的健
result_left = pd.merge(left, right, how="left", on=["key1", "key2"])
print(result_left)
print("**" * 50)

result_right = pd.merge(left, right, how="right", on=["key1", "key2"])
print(result_right)
print("**" * 50)

df1 = pd.DataFrame({
    "col1": [0, 1],
    "col_left": ["a", "b"]
})
df2 = pd.DataFrame({
    "col1": [1, 2, 2],
    "col_right": [2, 2, 2]
})
result_indicator = pd.merge(df1, df2, on="col1", how="outer", indicator=True)
# 指定连接键, 并集, 显示_merge列, 可以显示数据来源
print(result_indicator)

# 如果想要命名_merge列, 可以在指定indicator参数时直接对其命名
result_new_merge = pd.merge(df1, df2, on="col1", how="outer", indicator="indicatorc_column")
# 指定_merge列名称
print(result_new_merge)

# join()函数
left = pd.DataFrame({
    "A": ["A0", "A1", "A2"],
    "B": ["B0", "B1", "B2"],
}, index=["K0", "K1", "K2"])
right = pd.DataFrame({
    "C": ["C0", "C2", "C3"],
    "D": ["D0", "D2", "D3"]
}, index=["K0", "K2", "K3"])

result_join = left.join(right)  # 连接
print(result_join)
print("**" * 50)

# join()获取一个可选on参数, 该参数可以是一列或多列名称
# 它指定传递的DataFrame对齐在列上DataFrame
# 以下这两个函数调用完全等效
# left.join(right, on=key_or_keys)
# pd.merge(left, right, left_on=key_or_keys, right_index=True, how="left", sort=False)

# 新DataFrame对象
left = pd.DataFrame({
    "A": ["A0", "A1", "A2", "A3"],
    "B": ["B0", "B1", "B2", "B3"],
    "key": ["K0", "K1", "K0", "K1"]
})
right = pd.DataFrame({
    "C": ["C0", "C1"],
    "D": ["D0", "D1"]
}, index=["K0", "K1"])

result_new = left.join(right, on="key")  # 连接
print(result_new)
