import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression



# np.random.seed(666)
# x = np.random.uniform(-3, 3, size=100)
# x = x.reshape(-1, 1)  # 转换为二维数组供sklearn使用
# y = 0.5 * x**2 + x + 2 + np.random.normal(0, 1, size=100)
# # 使用线性回归拟合
# estimator = LinearRegression()
# estimator.fit(x, y)
# y_predict = estimator.predict(x)

# 绘制图形
# plt.scatter(x, y)  # x会自动展平，与y匹配
# plt.plot(x, y_predict, color='r')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Linear Regression on Quadratic Data')
# plt.show()

# #计算均方误差
# from sklearn.metrics import mean_squared_error
# mean_squared_error(y,y_predict)
#
# #添加二次项，绘制图像
# x2=np.hstack([x,x**2])
# estimator2=LinearRegression()
# estimator2.fit(x2,y)
# y_predict2=estimator2.predict(x2)
# plt.scatter(x,y)
# plt.plot(np.sort(x),y_predict2[np.argsort(x)],color='r')
# plt.show()

#计算均分误差和准确率
# from sklearn.metrics import mean_squared_error
# mean_squared_error(y,y_predict2)





