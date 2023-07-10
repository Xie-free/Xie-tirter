import pandas as pd

# concat()函数执行延轴执行连接操作
df1 = pd.DataFrame({
    "A": ["A0", "A1", "A2", "A3"],
    "B": ["B0", "B1", "B2", "B3"],
    "C": ["C0", "C1", "C2", "C3"],
    "D": ["D0", "D1", "D2", "D3"],
}, index=[0, 1, 2, 3])
df2 = pd.DataFrame({
    "A": ["A4", "A5", "A6", "A7"],
    "B": ["B4", "B5", "B6", "B7"],
    "C": ["C4", "C5", "C6", "C7"],
    "D": ["D4", "D5", "D6", "D7"],
}, index=[4, 5, 6, 7])
df3 = pd.DataFrame({
    "A": ["A8", "A9", "A10", "A11"],
    "B": ["B8", "B9", "B10", "B11"],
    "C": ["C8", "C9", "C10", "C11"],
    "D": ["D8", "D9", "D10", "D11"],
}, index=[8, 9, 10, 11])
frames = [df1, df2, df3]
result = pd.concat(frames, keys=["x", "y", "z"])  # 连接三个数据帧, 指定片段
result = result.loc["y"]  # 访问片段
print(result)

# 通过axis参数,我们可以确定行列维度

df4 = pd.DataFrame({
    'B': ['B2', 'B3', 'B6', 'B7'],
    'D': ['D2', 'D3', 'D6', 'D7'],
    'F': ['F2', 'F3', 'F6', 'F7']
}, index=[2, 3, 6, 7])
result1 = pd.concat([df1, df4], axis=0, sort=False)  # 列维度
result2 = pd.concat([df1, df4], axis=1, sort=False)  # 行维度
print(result1)
print(result2)

# 其中join参数的默认值为outer, 表示并集. 可以根据需求指定为inner表示交
result_3 = pd.concat([df1, df4], axis=0, sort=False, join="inner")  # 列维度,交集
result_4 = pd.concat([df1, df4], axis=1, sort=False, join="inner")  # 行维度,交集
print(result_3)
print(result_4)