#lise列表
#定义语法：[元素，元素....]
#索引语法：列表[标号]
name_list=["heima",666,False] #元素的数据类型可以不同
my_list=[[1,2,3],[4,5,6]]  #嵌套列表
print(my_list)
print(type(my_list))
print(name_list)
print(type(name_list))
#从前往后0开始，从后往前-1开始
print(name_list[-1])
print(name_list[-2])
#print(name_list[-3]) 列表索引超出范围
print(name_list[-3])
print(name_list[0])
print(name_list[1])
print(name_list[2])
print(my_list[0])
print(my_list[1])
print(my_list[0][1])
print(my_list[1][2])