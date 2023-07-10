def car(year, model):
    change = input("是否输入品牌(yes/no):")
    if change == "yes":
        brand = input("请输入汽车品牌:")
        return f"这是一辆{year}年生产, 型号是{model}的{brand}汽车"
    else:
        return f"这是一辆{year}年生产, 型号是{model}的宝马汽车"


print(car(input("请输入汽车年份:"), input("请输入汽车型号:")))

