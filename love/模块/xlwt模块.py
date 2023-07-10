import xlwt


work_book = xlwt.Workbook(encoding="utf-8")  # 创建work_book对象
work_sheet = work_book.add_sheet("sheet1")   # 创建工作表
for i in range(0, 9):
    # 打印九九乘法表在exel表格里
    for j in range(0, i+1):
        work_sheet.write(i, j, f"{j+1} * {i+1} = {(i+1)*(j+1)}")  # 写入数据,第一个为行,第二个为列,第三个为内容
else:
    work_book.save("test.xls")  # 保存数据表