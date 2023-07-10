"""
    article
        --- models.py
        --- __init__.py
    user
        --- models.py
            --- User
        --- __init__.py
        --- test.py

"""

# 用户发表文章
# 创建用户对象

# 发表文章, 文章对象

# from models import User  # 当前目录下的models里面的User类
# from 模块.user.models import User
from 模块.article.models import Article
from 模块.user.models import User

user = User("xie", 123456)  # ----> user就是通过导入User类

article = Article("完美世界", "辰东")

user.publish_article(article)

list1 = [1, 3, 5, 7, 9]
from 模块.模块使用方法.calculate import add

a = add(*list1)
print(a)

Max = 10000