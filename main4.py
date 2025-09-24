if int(input("你的身高是多少："))>120:
    print("你的身高超出限制，不可以免费")
    print("但是，如果vip级别大于3，可以免费")


    if int(input("你的vip级别是多少:"))>3:
        print("恭喜你，vip级别达标，可以免费游玩")
    else:
        print("vip级别不达标，需要买票")
else:
    print("你的身高符合标准，可以免费游玩")