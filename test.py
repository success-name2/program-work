# import torch
#
# print(torch.__version__)
# print(torch.version.cuda)
# print(torch.cuda.is_available())  # 输出为True，则安装成功
# import torch
# x0 = torch.tensor(2) #0阶张量，形状为torch.Size([])，亦写为()
# x1 = torch.tensor([2]) #1阶张量，形状为torch.Size([1])，亦写为(1)
# x2 = torch.tensor([2,3]) #1阶张量，形状为torch.Size([2])，亦写为(2)
# x3 = torch.tensor([[2,3,4], #2阶张量，形状为torch.Size([2, 3])，亦写为(2, 3)
# [5,6,7]])
# x4 = torch.tensor([[2,3,4], #2阶张量，形状为torch.Size([3, 3])，亦写为(3, 3)
# [5, 6, 7],
# [8, 9, 10]])
# print('x0的阶数为：{}，形状为：{}'.format(x0.ndim, x0.size()))
# print('x1的阶数为：{}，形状为：{}'.format(x1.ndim, x1.size()))
# print('x2的阶数为：{}，形状为：{}'.format(x2.ndim, x2.size()))
# print('x3的阶数为：{}，形状为：{}'.format(x3.ndim, x3.size()))
# print('x4的阶数为：{}，形状为：{}'.format(x4.ndim, x4.size()))
# 在 Python 中测试
# import matplotlib
# import matplotlib.pyplot as plt
# print("Matplotlib 版本:",matplotlib.__version__)
# # 设置字体为 SimHei（黑体）
# plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
# plt.rcParams['axes.unicode_minus'] = False    # 用来正常显示负号
# plt.plot([1, 2, 3, 4], [1, 4, 2, 3])
# plt.xlabel('一些数字')
# plt.ylabel('其他数字')
# plt.title('测试中文标题')
# plt.show()

# try:
#     import numpy as np
#     print("✅ NumPy 导入成功")
#     print("NumPy 版本:", np.__version__)
#     print("NumPy 安装路径:", np.__file__)
# except ImportError as e:
#     print("❌ NumPy 导入失败:", e)

try:
    import pandas as pd
    print("✅ Pandas 导入成功")
    print("Pandas 版本:", pd.__version__)
    print("Pandas 安装路径:", pd.__file__)
except ImportError as e:
    print("❌ Pandas 导入失败:", e)








