# time模块
# 1. 时间戳
import time

t = time.time()
print(t)
# time.sleep(3)

t1 = time.time()
print(t1)

# 将时间戳转成字符串
s = time.ctime(t)
print(s)

# 将时间戳转成元组
t = time.localtime(t)
print(t)
print(t.tm_yday)
print(t.tm_hour)

# 将元组转成时间戳
tt = time.mktime(t)
print(tt)

"""
 %Y  Year with century as a decimal number.
    %m  Month as a decimal number [01,12].
    %d  Day of the month as a decimal number [01,31].
    %H  Hour (24-hour clock) as a decimal number [00,23].
    %M  Minute as a decimal number [00,59].
    %S  Second as a decimal number [00,61].
    %z  Time zone offset from UTC.
    %a  Locale's abbreviated weekday name.
    %A  Locale's full weekday name.
    %b  Locale's abbreviated month name.
    %B  Locale's full month name.
    %c  Locale's appropriate date and time representation.
    %I  Hour (12-hour clock) as a decimal number [01,12].
    %p  Locale's equivalent of either AM or PM.
"""
# 将元组的时间转成字符串
s = time.strftime("%Y-%m-%d %H:%M:%S")
print(s)

# 将字符串转成元组的方式
r = time.strptime("2022/06/23", "%Y/%m/%d")
print(r)
"""
time模块:
重点:
    time()
    sleep()
    strftime("格式)
了解:
    t = time.localtime(t)
    元组  -----> t.tm_year  t.tm_mon

"""
