def getPoint():
    x=10
    y=20
    return x,y
a, b = getPoint()

#判断是否是奇数
def isOdd(num):
    if num%2==0:
        return  False
    else:
        return True
print(isOdd(20))

x=1000
def test():
    x=100
    print(f"函数内部：{x}")
test()
print(f"函数外部:{x}")