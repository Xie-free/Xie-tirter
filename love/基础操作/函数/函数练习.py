def car(phone_number, basic_price=10):
    time = int(input("乘车时间(分钟)"))
    distance = int(input("乘车距离"))
    if 0 < distance <= 2:
        print(f"乘坐{time}时间,{distance},不超过两公里,起步价")
    elif distance > 2:
        money = time * 0.5 + ((distance - 2) * 5)
        print(f"乘坐{time}时间,路程{distance},价格为{money}")
    else:
        print("请输入准确路程")


car(18221835631)
