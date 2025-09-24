#成年人判断
age=int(input("请输入你的年龄:"))
if age>=18:
    print("您已经成年，游玩需要买票，10元")
    print("祝你游玩愉快！")
elif age==15:
    print("您的年龄过大，不便来游玩")
else:
    print("您的年龄过小，可以免费游玩")

