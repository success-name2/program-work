import numpy as np
import matplotlib.pyplot as plt

# 整理后的数据点
data_points = [
    (-1.0, 7.1), (-0.8, 7.3), (-0.7, 7.0), (-0.5, 6.9), (-0.4, 6.4),
    (-0.2, 6.0), (-0.1, 5.6), (0.1, 4.8), (0.3, 4.7), (0.4, 4.9),
    (0.6, 4.3), (0.7, 3.7), (0.9, 3.3), (1.1, 3.7), (1.2, 3.0),
    (1.4, 2.3), (1.5, 2.0), (1.7, 2.5), (1.8, 2.2), (2.0, 1.7)
]

# 转换为numpy数组
X = np.array([point[0] for point in data_points])
y = np.array([point[1] for point in data_points])

# 添加偏置项
X_with_bias = np.column_stack([np.ones(len(X)), X])


class LinearPerceptron:
    def __init__(self):
        self.weights = None

    def fit(self, X, y, learning_rate=0.01, epochs=1000):
        """使用梯度下降法训练线性感知器"""
        n_samples, n_features = X.shape
        self.weights = np.random.randn(n_features)

        for epoch in range(epochs):
            # 前向传播
            predictions = X.dot(self.weights)

            # 计算误差（均方误差）
            errors = predictions - y

            # 梯度下降更新权重
            gradients = (2 / n_samples) * X.T.dot(errors)
            self.weights -= learning_rate * gradients

            # 每100轮打印一次损失
            if epoch % 100 == 0:
                loss = np.mean(errors ** 2)
                print(f"Epoch {epoch}, Loss: {loss:.4f}")

    def predict(self, X):
        """预测"""
        return X.dot(self.weights)

    def get_equation(self):
        """获取拟合直线方程"""
        if self.weights is not None:
            return f"y = {self.weights[1]:.4f}x + {self.weights[0]:.4f}"
        return "Model not trained yet"


# 创建并训练感知器
perceptron = LinearPerceptron()
perceptron.fit(X_with_bias, y, learning_rate=0.01, epochs=1000)

# 打印结果
print("\n" + "=" * 50)
print("线性拟合结果:")
print(f"拟合直线方程: {perceptron.get_equation()}")
print(f"最终权重: w0(偏置) = {perceptron.weights[0]:.4f}, w1(斜率) = {perceptron.weights[1]:.4f}")

# 预测
predictions = perceptron.predict(X_with_bias)

# 可视化结果
plt.figure(figsize=(12, 6))

# 原始数据和拟合直线
plt.subplot(1, 2, 1)
plt.scatter(X, y, color='blue', label='原始数据点', alpha=0.7)
x_line = np.linspace(-1.2, 2.2, 100)
X_line_with_bias = np.column_stack([np.ones(len(x_line)), x_line])
y_line = perceptron.predict(X_line_with_bias)
plt.plot(x_line, y_line, color='red', linewidth=2, label='拟合直线')
plt.xlabel('x')
plt.ylabel('y')
plt.title('线性感知器拟合结果')
plt.legend()
plt.grid(True, alpha=0.3)

# 残差图
plt.subplot(1, 2, 2)
residuals = y - predictions
plt.scatter(X, residuals, color='green', alpha=0.7)
plt.axhline(y=0, color='red', linestyle='--')
plt.xlabel('x')
plt.ylabel('残差')
plt.title('残差图')
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# 计算评估指标
mse = np.mean((y - predictions) ** 2)
rmse = np.sqrt(mse)
r_squared = 1 - np.sum((y - predictions) ** 2) / np.sum((y - np.mean(y)) ** 2)

print("\n模型评估指标:")
print(f"均方误差 (MSE): {mse:.4f}")
print(f"均方根误差 (RMSE): {rmse:.4f}")
print(f"决定系数 (R²): {r_squared:.4f}")