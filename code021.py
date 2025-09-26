#使用open打开一个文件.
#f是一个文件对象
flist=[]
count=0
while True:
  f=open('D:\Dev-Cpp/NEWS.txt','r')
  count+=1
  print(f'打开文件的个数:{count}')


#print(f)
  #f.close() #关闭文件