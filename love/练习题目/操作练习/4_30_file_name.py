import random

filename = ""
s = "klasd;lfkasj;dlgkj;lkj;zxlkchbzx-cuoapsdufgasodiufqwkjehnrltasnemfas,.dfmn"
file = input("请输入文件名称")
file1 = file.endswith("jpg") or file.endswith("gif") or file.endswith("png")
file2 = file.rfind(".")
file5 = file[file2::]
file3 = file[0:file2]
print(file3)

if file1 == True:
    if len(file3) < 6:
        for i in range(6):
            index = random.randint(0, len(s) - 1)
            filename += s[index]
        file5 = str(filename) + file5
        print(f"成功上传文件{file}")
    else:
        print("file")
else:
    print("文件后缀错误,上传失败!")

# 随机字母和数字的组合:
# filename = ""
# s = "klasd;lfkasj;dlgkj;lkj;zxlkchbzx-cuoapsdufgasodiufqwkjehnrltasnemfas,.dfmn"
# for i in range(6):
#     index = random.randint(0, len(s)-1)
#     filename += s[index]
#
# print(filename)