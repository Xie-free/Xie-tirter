import random

# 总车辆
car_park = []


def enter():
    print("---------欢迎进入停车场---------")
    number = input("输入车牌号:")
    # 构建结构{'车牌':[0, 5]}  车停的时间: key为车牌, values为时间
    car = {number: [0]}
    # car添加到总车辆
    car_park.append(car)
    print(f"{number}已进入")


def go_out():
    print("正在出场")
    number = input("输入车牌号:")
    # 遍历获取每一辆车
    for car in car_park:  # {}
        # 判断车辆是否在总车辆内
        if number in car:
            # 记录结束时间
            time = random.randint(0, 24)
            time_record = car.get(number)
            time_record.append(time)
            # 计算花费
            money = time * 4
            print(f"车牌{number}停车{time}小时,应缴费:{money}")
            break
    else:
        print("车辆不在停车场内")


# 进场
enter()
go_out()
