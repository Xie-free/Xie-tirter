# 文件夹  包
# 非py文件  包: py 文件
# 一个包中可以存放多个模块
# 项目  >  包  >  模块  >  类  函数  变量

# 使用包中模块中的User类
# from user import models
#
# u = models.User("xie", 123456)
# u.show()

# from user.models import User
#
# u = User("xie", 123456)
# u.show()
#
# from article.models import Article
#
# a = Article("完美世界", "辰东")
# a.show()

# from user.models import *

# print(version)
# u = User("xie", 123456)

from user.models import version

"""
    article
        --- models.py
        --- __init__.py
    user
        --- models.py
        --- __init__.py
    
    包的导入.py

    from 包 import 模块
    from 包.模块 import 类|函数|变量
    from 包.模块 import *
"""
