import os

r = os.path.isabs(r"F:\python\python_word\quan.png")
print(r)


r = os.path.isabs("../第一课/hello")  # ../ 表示返回当前文件上一级   第一课
print("------->", r)

r = os.path.isabs("/第一课/hello")  # 找跟os.py同级的第一课里面的hello.py
print("------->", r)

# 获取路径: directory 目录 文件夹
# 当前文件所在文件夹路径
path = os.path.dirname(__file__)  # F:\Python\love\文件操作
print(path)

# 根据相对路径得到绝对路径
# F:\Python\love\文件操作\犬夜叉.png
path = os.path.abspath("犬夜叉.png")
print(path)

# 获取当前文件的绝对路径
path = os.path.abspath(__file__)
print(path)

# 当前文件的文件夹  类似于 os.path.dirname(__file__)
path = os.getcwd()
print(path)

r = os.path.isfile(os.getcwd())
print(r)

r = os.path.isdir(os.getcwd())
print(r)

# os.path

path = r"F:\Python\love\文件操作\os.py"
result = os.path.split(path)
print(result)  # ('F:\\Python\\love\\文件操作', 'os.py')
print(result[1])
# file_name = path[path.rfind("\\") + 1:]

result = os.path.splitext(path)  # 分割文件与扩展名
# 文件后缀
print(result)  # ('F:\\Python\\love\\文件操作\\os', '.py')

size = os.path.getsize(path)  # 获取单位大小, 单位是字节
print(size)

result = os.path.join(os.getcwd(), "file", "al.jpg")
print(result)
"""
os.path:  常用函数
dirname()
join()
splitext()
getsize()

isabs()  # 判断是不是绝对路径
isfile()  # 判断是不是一个文件
isdir()  # 判断是不是一个文件夹
"""