weather = input("How the weather?")
if weather !="sunny":
    print("bad weather,stay home.")
else:
    money = float(input("good weather,how much money?"))
    if money >= 500:
        print("go to the amusement park! ")
    elif money >= 300:
        print("go to the mall")
    elif money >= 50:
        print("go to the food street")
    else:
        print("no money,stay home")