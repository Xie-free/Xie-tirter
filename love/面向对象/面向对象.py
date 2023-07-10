"""
面向对象:
程序        现实中
对象   ------> 具体的事物

现实中事物  -----》 装成电脑程序
世界万物皆是对象

好处:

面向对象:
    类
    对象
    属性
    方法

对象:
    a的手机
    b的手机
    c的手机
    d的手机
    ....


    对象的集合 ------> 共同特征: 品牌  颜色  大小  价格           动作: 打电话  发短信  上网  打游戏

    类别:   手机类
            学生类
      a, b, c, d, f.....

      特征: 姓名  年龄  性别  身高  血型  婚否   ------> 属性
      动作: 刷抖音  敲代码  看书......  ----------> 方法

      多个对象   ------> 提取对象的共同特征和动作 -----> 封装到一个类



"""

# 所有的类名要求首字母大写, 多个单词使用驼峰式命名
# ValueError  TypeError  StopIterable
"""
class 类名[(父类)]:
    属性: 特征
    
    方法: 动作

"""


class Phone:
    pass
    # 属性
    brand = "华为"
    # 方法


# 使用类创建对象
a = Phone()

print(a)
print(a.brand)
a.brand = "iphone"
print(a.brand)

b = Phone()

print(b)
print(b.brand)
b.brand = "iphone xxs"
print(b.brand)

c = Phone()
print(c.brand)