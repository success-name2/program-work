#语法
#定义集合
my_set={"传智教育","黑马程序员","itma"}
my_set_empty=set()
print(f"my_set_empty的内容为:{my_set_empty},类型是{type(my_set_empty)}")

#添加元素
my_set.add("python")
my_set.add("传智教育")
print(f"my_set添加后结果是：{my_set}")

#移除元素
my_set.remove("黑马程序员")
print(f"移除后内容为：{my_set}")

#随机取出元素
element=my_set.pop()
print(f"集合被取出的元素是:{element}，取出后内容为:{my_set}")

#清空集合
#my_set.clear()
#print(f"集合被清空后内容为:{my_set}")

#取集合的差集
set1={1,2,3}
set2={1,5,6}
set3=set1.difference(set2)
print(f"取出差集的结果后，内容为:{set3}")

#消除两个集合的差集
#语法：集合1.difference_update(集合2)
set1={1,2,3}
set2={1,5,6}
set1.difference_update(set2)
print(f"消除后，集合1的内容为:{set1}")

#两个集合合并
set1={1,2,3}
set2={1,5,6}
set3=set1.union(set2)
print(f"两集合合并后的结果为:{set3}")

#统计集合的元素数量
set1={1,2,3,1,3,4,5,6,7,8,9,2}
set3=len(set1)
print(f"集合内的元素数量有{set3}个")

#集合的遍历
set1={1,2,3,1,3,4,5,6,7,8,9,2}
for element in set1:
    print(f"集合的元素有:{element}")

