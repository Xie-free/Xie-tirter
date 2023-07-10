import pandas as pd

df = pd.read_json("sites.json")
print(df.to_string())

# json对象与Python字典具有相同的格式
# 所以我们可以直接将Python字典转化为DataFrame数据
# 字典格式的JSON
s = {
    "col1": {"row1": 1, "row2": 2, "row3": 3},
    "col2": {"row1": "x", "row2": "y", "row3": "z"}
}
# 读取JSON转为DataFrame
df_1 = pd.DataFrame(s)
print(df_1)

# 从URL中读取JSON数据
URL = "https://static.runoob.com/download/sites.json"
df_2 = pd.read_json(URL)
print(df_2)

df_3 = pd.read_json("nested_list.json")
print(df_3)  # 显示的数据并不完全

# json_normalize()方法将内嵌的数据完整的解析出来
import json

# 使用Python JSON 模块载入数据
# with open("nested_list.json", "r") as f:
#     data = json.load(f.read())
#
# # 展平数据
# df_nested_list = pd.json_normalize(data, record_path=["students"])
# json_normalize() 使用了参数 record_path
# 并设置为 ['students'] 用于展开内嵌的 JSON 数据 students.
# 显示结果还没有包含 school_name 和 class 元素
# 如果需要展示出来可以使用 meta 参数来显示这些元数据.
# df_nested_list = pd.json_normalize(
#     data,
#     record_path =['students'],
#     meta=['school_name', 'class']
# )
# print(df_nested_list)