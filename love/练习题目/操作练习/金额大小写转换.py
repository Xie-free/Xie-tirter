import sys


def int_change(int_part):
    count = len(int_part)
    if count == 1:
        return chinese_num[int(int_part)] + "圆"
    elif count == 2:
        result = chinese_num[int(int_part[0])] + "拾" + chinese_num[int(int_part[1])] + "圆"
        return result
    elif count == 3:
        result = chinese_num[int(int_part[0])] + "佰" + chinese_num[int(int_part[1])] + "拾" + chinese_num[
            int(int_part[2])] + "圆"
        return result
    elif count == 4:
        result = chinese_num[int(int_part[0])] + "仟" + chinese_num[int(int_part[1])] + "佰" + chinese_num[
            int(int_part[2])] + "拾" + chinese_num[int(int_part[3])] + "圆"
        return result


def float_change(float_part):
    float_count = len(float_part)
    if float_count == 1:
        return chinese_num[int(float_part)]
    elif float_count == 2:
        result = chinese_num[int(float_part[0])] + "角" + chinese_num[int(float_part[1])] + "分"
        return result


if __name__ == "__main__":
    chinese_num = "零壹贰叁肆伍陆柒捌玖"
    num = sys.argv[1]  # 输入
    dian_index = num.find(".")  # 寻找"."的位置进行判断
    if dian_index == -1:  # 判断是否有小数部分
        int_part_result = int_change(num) + "整"  # 如果没有, 将直接调用int_change函数,然后将返回的数值加上 整
        print(int_part_result)
    else:
        int_part, float_part = num[0:dian_index], num[dian_index + 1:]  # 分别通过下标索引获得整数部分,和小数部分
        int_part_result = int_change(int_part)  # 整数返回的部分
        float_part_result = float_change(float_part)  # 小数返回的部分
        result_num = int_part_result + float_part_result  # 将两者拼接
        print(result_num)
