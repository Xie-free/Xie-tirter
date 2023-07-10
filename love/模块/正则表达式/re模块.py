# 正则表达式: 字符串模式(判断字符串是否符合一定的标准)
import re  # 导入模块

# 创建模式对象

# pat = re.compile("AA")  # 此处的AA, 是正则表达式用来验证其他的字符串
# m = pat.search("ABCDAA")  # search里面的字符串为被校验的内容
# n = pat.search("ABAACDAAEAA")  # search方法.进行对比查找,只查找第一个

# 没有模式对象
# n = re.search("SAD", "SADFG")  # 前面的字符串是规则, 后面的字符串为被校验

# a = re.findall("a", "ASaasdAaSDF")

# a = re.findall("[a-z]", "ASaasdAaSDF")

# sub

print(re.sub("写", "谢", "我写写你"))  # 查找"我写写你"这个字符串把写替换成谢

