str1="hello"
str2="world"
str3="please"
def data_len(data):
    count=0
    for i in data:
        count+=1
        print(f"字符串data的长度为:{count}")

data_len(str1)
data_len(str2)
data_len(str3)