# import torch
#
# print(torch.__version__)
# print(torch.version.cuda)
# print(torch.cuda.is_available())  # 输出为True，则安装成功
import torch
x0 = torch.tensor(2) #0阶张量，形状为torch.Size([])，亦写为()
x1 = torch.tensor([2]) #1阶张量，形状为torch.Size([1])，亦写为(1)
x2 = torch.tensor([2,3]) #1阶张量，形状为torch.Size([2])，亦写为(2)
x3 = torch.tensor([[2,3,4], #2阶张量，形状为torch.Size([2, 3])，亦写为(2, 3)
[5,6,7]])
x4 = torch.tensor([[2,3,4], #2阶张量，形状为torch.Size([3, 3])，亦写为(3, 3)
[5, 6, 7],
[8, 9, 10]])
print('x0的阶数为：{}，形状为：{}'.format(x0.ndim, x0.size()))
print('x1的阶数为：{}，形状为：{}'.format(x1.ndim, x1.size()))
print('x2的阶数为：{}，形状为：{}'.format(x2.ndim, x2.size()))
print('x3的阶数为：{}，形状为：{}'.format(x3.ndim, x3.size()))
print('x4的阶数为：{}，形状为：{}'.format(x4.ndim, x4.size()))