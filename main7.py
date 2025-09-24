import random
num=random.randint(1,10)
count=0
#通过一个布尔类型变量，做循环是否继续的标记
flag=True
while flag:
    guess_num=int(input("请输入你要猜测的数字："))
    count+=1
    if guess_num==num:
        print("恭喜你，猜中了！")
        flag=False
    else:
        if guess_num>num:
            print("你猜的数字大了")
        else:
            print("你猜的数值小了")
print(f"你总共猜了{count}次")
