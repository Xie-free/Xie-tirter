import pandas as pd

# # 从 CSV 文件中读取数据
# df = pd.read_csv('data.csv')
#
# # 从 Excel 文件中读取数据
# df = pd.read_excel('data.xlsx')
#
# # 从 SQL 数据库中读取数据
# import sqlite3
#
# conn = sqlite3.connect('database.db')
# df = pd.read_sql('SELECT * FROM table_name', conn)
#
# # 从 JSON 字符串中读取数据
# json_string = '{"name": "John", "age": 30, "city": "New York"}'
# df = pd.read_json(json_string)
#
# # 从 HTML 页面中读取数据
# url = 'https://www.runoob.com'
# dfs = pd.read_html(url)
# df = dfs[0]  # 选择第一个数据框
