num=100 #全局变量
def test_a():
    #num=100  #局部变量
    print(num)
def add_a():
    b=100
    global num #设置内部定义的变量为全局变量
    num=10
    print(b+num)

add_a()
test_a()