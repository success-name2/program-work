#定义元组语法：(元素，元素，.....元素)
t1=(1,"hello",True)
t2=()
t3=tuple()
print(f"t1的类型为{type(t1)},内容为{t1}")

#定义单个元素的元组
t4=("hello",)
print(f"t4的类型为{type(t4)},内容为{t4}")

#元组的嵌套
t5=((1,2,3),(4,5,6))
print(f"t5的类型为{type(t5)},内容为{t5}")
print(t5[1][1])

#元组的操作
t6=("传智教育","黑马程序员","python")
index=t6.index("黑马程序员")
print(f"黑马程序员的下标为：{index}")

#count计数
t7=("传智教育","黑马程序员","python","please")
num=t7.count("黑马程序员")
print(num)
print(len(t7))

#元组的遍历
index=0
while index<len(t7):
  print(f"元组{t7[index]}")
  index+=1

#元组的for遍历
for element in t7:
    print(f"元组中的元素为：{element}")