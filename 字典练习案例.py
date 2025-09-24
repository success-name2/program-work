info_dict={
    "王力宏":{
        "部门":"科技部",
        "工资":3000,
        "级别":2,
    },
    "林俊杰":{
        "部门": "市场部",
        "工资": 4000,
        "级别": 1,
    },
    "张学友":{
        "部门": "市场部",
        "工资": 6000,
        "级别": 2,
    },
    "刘德华":{
        "部门": "科技部",
        "工资": 5000,
        "级别": 1,
    },
}
print(f"员工在升职加薪前的结果:{info_dict}")
for name in info_dict:
    if info_dict[name]["级别"]==1:
        employee_info_dict=info_dict[name]
        employee_info_dict["级别"]=2
        employee_info_dict["工资"]=employee_info_dict["工资"]+1000
        info_dict[name]=employee_info_dict

print(f"员工在升职加薪后的结果:{info_dict}")