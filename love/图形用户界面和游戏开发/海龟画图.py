import turtle
from time import sleep

t = turtle.Pen()  # 定义一个画笔,此时小光标在(0,0)位置
t.fd(100)  # 向前运动100像素
t.left(120)  # 向左转120°
t.fd(100)  # 继续向前运动100像素
t.left(120)
t.fd(100)

t.shape("turtle")  # 改变画笔的形状

sleep(10)
