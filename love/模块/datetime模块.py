# datetime: time 模块升级版
"""
datetime模块:
    time  时间
    date  日期  (date 数据)
    datetime  日期时间  now()
    timedelta  时间差  timedelta(days="", weeks = ""....)
"""
import datetime
import time

print(datetime.time.hour)  # 对象
print(time.localtime().tm_hour)

# 因为date是类, 所以要求创建对象
d = datetime.date(2022, 6, 23)
print(datetime.date.day)
print(time.time())
print(datetime.date.ctime(d))

# datetime, timedelta
print(datetime.date.today())  # 2022-06-17

# 时间差
time_del = datetime.timedelta(days=3, hours=3)
print(time_del)

# datetime.datetime.now()  ---->  得到当前的日期和时间
now = datetime.datetime.now()
print(now)
result = now + time_del
print(result)

# 缓存: 数据redis  作为缓存  redis.set(key, value, 时间差)  会话: session



