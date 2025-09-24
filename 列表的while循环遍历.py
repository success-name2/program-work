#使用while循环遍历列表中的元素
def she_list_while_func():
    she_list=["传智教育","黑马程序员","python"]
    index=0
    while index<len(she_list):
        element=she_list[index]
        print(f"列表的元素：{element}")
        index+=1
she_list_while_func()

#for循环遍历列表
def my_list_for_func():
    my_list=[1,2,3,4,5]
    for element in my_list:
        print(f"列表元素有:{element}")
my_list_for_func()