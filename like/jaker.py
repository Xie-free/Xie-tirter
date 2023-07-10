My_Name = 'Tom'
print(My_Name)
SchoolName = '群星职校'
print(SchoolName)
# int 指整数
numb2 = 1.1
numb1 = 1
# float 指浮点数
print(type(numb1))
print(type(numb2))
# str 指字符，英文字母，要带引号
a = "hello world"
print(type(a))
# bool 布尔型，通常判断使用，布尔型有两个取值 Ture 和 False
b = True
print(type(b))

import turtle

turtle.pensize(4)
turtle.pencolor('green')

turtle.forward(180)
turtle.right(90)
turtle.forward(180)
turtle.right(90)
turtle.forward(180)
turtle.right(90)
turtle.forward(180)

turtle.mainloop()
