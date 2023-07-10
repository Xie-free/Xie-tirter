def word(input_word):
    input_word.sort()  # 排序
    i = 0  # 设定初始值
    while i < len(input_word):  # 获取列表下表
        result = input_word.count(input_word[i])  # 获取数量
        print(f"{input_word[i]}:{result}")  # 打印
        if result >= 1:  # 判断是否大于1
            i += result  # 然后进行下标值的修改
        else:
            i += 1


if __name__ == '__main__':
    input_word_ = input("请输入一串英文,其中单词之间用空格隔开").split()
    word(input_word_)
