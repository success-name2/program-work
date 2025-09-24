my_list=[1,2,3,4,5]
my_tuple=(1,2,3,4,5,6)
my_str="abcdefg"
my_set={1,2,3,4,5,6}
print(len(my_list))
print(len(my_str))
print(max(my_list))
print(max(my_str))
print(min(my_str))
print(min(my_list))

#容器转列表
print(f"元组转列表的结果是:{list(my_tuple)}")
print(f"字符串转列表的结果是:{list(my_str)}")
#容器转元组
print(f"元组转元组的结果是:{tuple(my_tuple)}")
print(f"字符串转元组的结果是:{tuple(my_str)}")
#容器转字符串
print(f"元组转字符串的结果是:{str(my_tuple)}")
print(f"字符串转字符串的结果是:{str(my_str)}")
#容器转集合
print(f"元组转集合的结果是:{set(my_tuple)}")
print(f"字符串转集合的结果是:{set(my_str)}")
#sorted排序
print(f"列表对象的排序结果:{sorted(my_list)}")
print(f"字符串对象的排序结果:{sorted(my_str)}")
print(f"元组对象的排序结果:{sorted(my_tuple)}")

print(f"列表对象反向的排序结果:{sorted(my_list, reverse=True)}")
print(f"字符串对象反向的排序结果:{sorted(my_str, reverse=True)}")
print(f"元组对象反向的排序结果:{sorted(my_tuple, reversr=True)}")