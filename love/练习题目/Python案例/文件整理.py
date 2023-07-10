# 同学们在网上冲浪的过程中，收集了很多资料，放在“备用资料”文件夹中。
# 随着时间推移，文件夹中的内容比较凌乱。
# 每隔一段时间我们应该对文件夹进行必要的整理，对其进行分类。
# （1）	在“备用资料”文件夹中建立名为“图片”、“文本”和“声音”三个文件夹。
import os  # 导入文件模块


def get_dir(file_path):
    if "文本" not in file_name:  # 判断文本这个文件夹在不在里面,如果不在则创建,以下如同
        os.mkdir(file_path + r"\文本")
    elif "音乐" not in file_name:
        os.mkdir(file_path + r"\音乐")
    elif "图片" not in file_name:
        os.mkdir(file_path + r"\图片")


def file_read_write(read_file, write_file, write_file_name):  # 读文件和写文件的地址
    with open(read_file, "rb") as f:  # 打开文件,权限为读取
        content = f.read()  # 读取文件内容
        with open(write_file + f"\\{write_file_name}", "wb") as w:  # 打开文件夹,权限为写
            w.write(content)  # 写入图片


def move_file(file_path):
    move_dict = set()
    for i in file_name:  # 遍历获得所有文件
        file_path_name = file_path + "\\" + f"{i}"  # 拼接路径和文件名
        if os.path.isfile(file_path_name):  # 判断文件是否为文件
            move_dict.add(file_path_name)
            file_text = os.path.splitext(file_path_name)  # 文件路径和文件后缀
            file_suffix = file_text[1]
            if file_suffix == ".jpg" or file_suffix == ".gif":  # 判断文件是否为图片
                file_read_write(file_path_name, file_path + r"\图片", i)  # 调用函数
            elif file_suffix == ".wav" or file_suffix == ".mp3" or file_suffix == ".mid":
                # 判断文件是否为音乐
                file_read_write(file_path_name, file_path + r"\音乐", i)  # 调用函数
            elif file_suffix == ".rtf" or file_suffix == ".txt" or file_suffix == ".doc" or file_suffix == ".html":
                # 判断文件是否为文本
                file_read_write(file_path_name, file_path + r"\文本", i)
        else:
            continue
    else:
        for i in move_dict:
            os.remove(i)


if __name__ == '__main__':
    file_path_ = r".\备用资料"
    file_name = os.listdir(file_path_)  # 获取文件夹所有文件名
    get_dir(file_path_)  # 判断文件夹是否存在,不存在则创建
    move_file(file_path_)
