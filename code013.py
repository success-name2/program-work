a=int(input("请输入一个数:"))
if a>0:
    print("整数")
elif a<0:
    print("负数")
else:
    print("0")
#判断闰年
year=int(input("请输入一个年份:"))
if year%100==0:
    if year%400==0:
        print("闰年")
    else:
        print("平年")
else:
    if year%4==0:
        print("闰年")
    else:
        print("平年")
