my_str="itheima and itcast"
#通过下标索引取值
value=my_str[2]
value2=my_str[-16]
print(value)
print(value2)

#index方法
value3=my_str.index("and")
print(value3)

#字符串的操作
#字符串替换
new_my_str=my_str.replace("it","程序")
print(new_my_str)

#字符去除
my_str="hello heimacast itcast"
new_my_str=my_str.strip('he')
print(new_my_str)

#统计个数
my_str="hello heimacast itcast"
count=my_str.count("it")
print(count)

#统计字符串长度
num=len(my_str)
print(num)




