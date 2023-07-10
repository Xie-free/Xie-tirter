# 判断是否为整数
def car_money(km, wait_time):
    if isinstance(km, int):
        if 0 < km <= 15:
            print(f"乘车{km}公里,等待时间为{wait_time}分钟,加收{wait_time}元,"
                  f"价格为{round((13 + ((km - 3) * 2.3)) + wait_time, 1)}")
        elif km > 15:
            money = (13 + (15 * 2.3))
            return f"乘车{km}公里,等待时间为{wait_time}分钟, 加收{wait_time}元,"f"价格为{round((money + (km - 15) * (2.3 * 1.5)) + wait_time, 1)}元"
        else:
            return "请输入有效整数"
    else:
        return "请输入整数"


if __name__ == '__main__':
    km_car = eval(input("请输入乘车里程(整数):"))  # 输入乘车里程
    wait_time_car = eval(input("请输入等待时间(分钟):"))  # 输入等待时间
    print(car_money(km_car, wait_time_car))
