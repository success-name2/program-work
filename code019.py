a= {'id': 1, 'name': 'zhansan', 100: 'list', 'score': 100}
#新增键值对
print(a)

#字典中根据key修改value，也使用[]来进行的~
a['score']=90
print(a)
a['name']='lisi'
print(a)

#使用pop方法根据key删除键值对~
a.pop('name')
print(a)
a.pop('score')
print(a)

#字典的遍历操作
#for循环遍历字典
for key in a:
    print(key,a[key])

print(a.keys())
print(a.values())
print(a.items())
#通过for循环获取key,value的值
for key,value in a.items():
    print(key,value)



