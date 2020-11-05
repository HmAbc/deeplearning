#!/user/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

# 阶跃函数简单实现，但是只支持实数
# def step_function(x):
#     if x > 0:
#         return 1
#     else:
#         return 0

# 重新编写函数，使之支持numpy数组
def step_function(x):
    y = x > 0
    return y.astype(np.int)

# 画出阶跃函数图像
# x = np.arange(-5, 5, 0.1)
# y = step_function(x)
# plt.plot(x, y)
# plt.ylim(-0.1, 1.1)
# plt.show()

# sigmoid 函数
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# ReLU 函数
def ReLU(x):
    return np.maximum(0, x)