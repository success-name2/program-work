a=10
b=20
c=30
print(a < b < c) #链式比较
print(a>b and b<c)
print(a > b > c)

print(a<b or b<c)
print(a>b or b<c)
print(a>b or b>c)

print(not a<b)
print(not a>b)

#短路求值
print(a>b and c/10==3)
print(a<b and c%10==0)