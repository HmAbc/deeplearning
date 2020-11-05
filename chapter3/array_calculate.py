#!/user/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

# 生成一维数组
A = np.array([1, 2, 3, 4])
# print(A)
# print(np.ndim(A))
# print(A.shape)

# 生成二维数组
B = np.array([[1, 2], [3, 4], [5, 6]])
# print(B)
# print(np.ndim(B))
# print(B.shape)

C = np.array([[1, 2, 3], [4, 5, 6]])
# 矩阵点乘
D = np.dot(B, C)

print(D)

E = np.array([1, 2])
F = np.array([[1, 2, 3], [4, 5, 6]])
G = E @ F
print(G)