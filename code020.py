#使用hash函数计算出一个变量的hash值
print(hash(0))
print(hash(3.14))
print(hash('hello'))
print(hash(True))
print(hash((1,2,3)))

#有些类型不能计算hash值,即可变对象不能计算hash值。
# # print(hash([1,2,3]))
# a={
#     'id':1,
#     'num':2
# }
# print(hash(a))


