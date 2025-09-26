#创建字典
a={}
print(type(a))
b=dict()
print(type(b))

#设置初值
#a={'id':1,'name':'zhangsan','value':'name'}
a={
    'id':1,
    'name':'zhangsan',
    100:'list',
    'classid':'4'
}
#用in判断某个key是否存在
print('id' in a)
print('name' in a)
print('name' not in a)
print(a['name'])
print(a['id'])
print(a[100])
print(a['classid'])

