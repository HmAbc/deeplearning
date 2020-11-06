#!/user/bin/env python3
# -*- coding: utf-8 -*-

# 实现第一层的神经元，两个输入，第一层三个神经元

import numpy as np

# 定义输入
X = np.array([1.0, 0.5])
# 定义第一层权重
W1 = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
# 定义第一层的偏置
B1 = np.array([0.1, 0.2, 0.3])

# 第一层神经元的输出
A1 = np.dot(X, W1) + B1 # 矩阵乘法也可以写成 X @ W1

# 定义激活函数 sigmoid
def sigmoid(x):
    return 1/(1 + np.exp(-x))

# 经过激活函数后的输出
Z1 = sigmoid(A1)

print(A1)
print(Z1)

# 下面实现第一层到第二层的信号传递，第二层有两个神经元
W2 = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
B2 = np.array([0.1, 0.2])

A2 = np.dot(Z1, W2) + B2
Z2 = sigmoid(A2)

print(A2)
print(Z2)

# 第二层到输出层的信号传递，输出层有两个输出
def identity_function(x):
    return x

W3 = np.array([[0.1, 0.3], [0.2, 0.4]])
B3 = np.array([0.1, 0.2])

A3 = Z2 @ W3 + B3
Z3 = identity_function(A3)