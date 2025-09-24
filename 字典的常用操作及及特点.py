my_dict={"周杰伦":99,"林俊杰":98,"龚成":97}
#新增元素
my_dict["张信哲"]=66
print(f"增加元素后结果为:{my_dict}")

#更新元素
my_dict["周杰伦"]=33
print(f"更新元素后结果为:{my_dict}")

#删除元素
score=my_dict.pop("周杰伦")
print(f"字典中移除一个元素后结果为:{my_dict},周杰伦的分数为:{score}")

#清空字典
my_dict.clear()
print(f"清空后字典的内容为:{my_dict}")

#获取全部的key
my_dict={"周杰伦":99,"林俊杰":98,"张学友":97}
keys=my_dict.keys()
print(f"字典中的全部keys是：{keys}")

#遍历字典
for key in keys:
    print(f"字典的key是:{key}")
    print({my_dict[key]})

#统计字典中的元素数量
num=len(my_dict)
print(f"字典中的元素个数为:{num}")