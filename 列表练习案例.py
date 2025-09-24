her_list=[21,25,21,23,22,20]
her_list.append(31)
print(f"追加31后列表值为：{her_list}")
her_list1=[29,33,30]
her_list.extend(her_list1)
print(f"“追加新列表后,列表值为：{her_list}")

num1=her_list[0]
print(num1)

num2=her_list[-1]
print(num2)

index=her_list.index(31)
print(index)