import tkinter


# 创建应用程序主窗口对象
root = tkinter.Tk()

# 创建按钮(Button)
btn01 = tkinter.Button(root)
# 文本框
btn01["text"] = "点我就送我烟花"
# 几何布置管理器, 管理组件的大小和位置
btn01.pack()
#


root.mainloop()  # 调用组件的mainloop()方法, 进入事件循环