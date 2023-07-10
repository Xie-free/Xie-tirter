"""
当你导入一个模块，Python 解析器对模块位置的搜索顺序是:
1、当前目录
2、如果不在当前目录，Python 则搜索在shell 变量PYTHQVPATH 下的每个目录。
3、如果都找不到，Python会察看默认路径。UNIX下，默认路径一 般为usr/ local/lib python/。
模块搜索路径存储在system 模块的sys. path变量中。变量里包含当前目录，PYTHOVPATH和由安装过程决定的默认目录。
"""

"""
自定义模块
系统模块:
    sys模块
    
"""

import sys
import random
print(sys.path)
print(sys.version)
print(sys.argv)  # 运行程序时的参数, avgv是一个列表