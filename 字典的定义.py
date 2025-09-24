#定义字典
my_dict={"王力宏":99,"龚成":99,"孙悟空":90}
#定义空字典
my_dict2={}
my_dict3=dict()
print(f"字典1的内容是：{my_dict},类型是:{type(my_dict)}")
print(f"字典2的内容是：{my_dict2},类型是:{type(my_dict2)}")
print(f"字典3的内容是：{my_dict3},类型是:{type(my_dict3)}")
#定义重复key字典
my_dict={"王力宏":99,"龚成":99,"孙悟空":90}
print(f"重复字典的内容为:{my_dict}")

#通过key获取value
my_dict={"王力宏":99,"龚成":99,"孙悟空":90}
score= my_dict["龚成"]
print(score)

#定义嵌套字典
stu_score_dict={
   "王力宏": {
       "语文":77,
       "数学":80,
       "英语":90,
   },
    "周杰伦":{
       "语文":67,
       "数学":83,
       "英语":90,
    },
    "林俊杰": {
       "语文":99,
       "数学":80,
       "英语":60
    }
}
print(f"学生的考试信息为：{stu_score_dict}")
score=stu_score_dict["林俊杰"]["语文"]
print(f"林俊杰的语文成绩为:{score}")







