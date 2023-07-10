print('abc'.isidentifier())  # abc可以作为Python变量名
print('3abc'.isidentifier())  # 变量名不能以数字开头
print('_3abc'.isidentifier())
print('__3abc'.isidentifier())
print(',__3abc'.isidentifier())  # 变量名不能以标点符号开头
print('__3abc('.isidentifier())  # 变量名中也不能含有标点符号
print('a,bc'.isidentifier())
