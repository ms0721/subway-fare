location = input("去那吃饭？")
money = float(input("准备多少预算"))
if location == "汇聚":
    if money >= 1000:
        print("大玩特玩")
    elif money >= 500:
        print("海底捞")
    elif money >=200:
        print("炒菜饭店")
    elif money >= 100:
        print("争先","元气寿寺")
    elif money >= 50:
        print("王繁星","宜家餐厅")
    elif money >= 30:
        print("米村","麦当劳","阳阳")
    else:
        print("预算不足")
elif location =="天街":
    if money >= 1000:
        print("大玩特玩")
    elif money >= 500:
        print("海底捞")
    elif money >= 200:
        print("炒菜饭店")
    elif money >= 100:
        print("绿茶餐厅")
    # elif money >= 50:
    #     print("")
    elif money >= 30:
        print("米村", "麦当劳", "阳阳","萨里亚")
    else:
        print("预算不足")
else:
    print("未知地点")