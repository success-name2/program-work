#查找元素下标
#语法：列表.index(元素)
my_list=["itcast","itheima","python"]
index=my_list.index("itheima")
print(f"itheima在列表中的索引下标值为：{index}")
#index=my_list.index("hello")
#print(f"hello在列表中的索引下标值为：{index}"),不在列表中

#修改特定元素索引值
my_list[0]="传智教育"
print(f"列表被修改后，值为：{my_list}")

#在指定位置插入元素
my_list.insert(1,"best")
print(f"插入元素后，列表的值为：{my_list}")

#在列表尾部追加单个元素
my_list.append("黑马程序员")
print(f"追加元素后，列表值为：{my_list}")

#在列表尾部追加一批元素
my_list2=[1,2,3]
my_list.extend(my_list2)
print(f"追加一个新的列表后，列表值为：{my_list}")

#删除列表值
#del my_list[2]
#print(f"列表删除元素后结果为：{my_list}")

element=my_list.pop(2)
print(f"取出元素后列表为:{my_list},取出的元素为：{element}")

#删除某元素在列表中的第一个匹配项
my_list.remove("传智教育")
print(f"移除后列表值为：{my_list}")

#清空列表
#my_list.clear()
#print(f"清空后列表为：{my_list}")

#统计指定元素个数
count=my_list.count("传智教育")
print(f"列表中传智教育的数量为：{count}")

#统计列表中全部元素的数量
count=len(my_list)
print(f"列表中元素数量总共有：{count}个")