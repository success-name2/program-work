her_str="万过薪月, 员序程马黑来, nohtyp学"
result=her_str[::-1][9:14]
print(result)
result2=her_str[5:10][::-1]
print(result2)
result3=her_str.split(", ")[1].replace("来", "")[::-1]
print(result3)