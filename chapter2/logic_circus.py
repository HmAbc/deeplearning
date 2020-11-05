#!/user/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

# 定义与门
# def AND(x1, x2):
#     w1, w2, theta = 0.5, 0.5, 0.7
#     tmp = x1 * w1 + x2 * w2
#     if tmp <= theta:
#         return 0
#     else:
#         return 1

# print(AND(0, 0))
# print(AND(1, 0))
# print(AND(0, 1))
# print(AND(1, 1))

# 使用权重和偏执实现与门
def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    temp = np.sum(w*x) + b
    if temp <= 0:
        return 0
    else:
        return 1

# 实现与非门，或门和他们俩的实现方式一样，只有权重和偏置不一样
def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])  # 只有权重不一样
    b = 0.7
    temp = np.sum(w*x) + b
    if temp <= 0:
        return 0
    else:
        return 1

def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    temp = np.sum(w*x) + b
    if temp <= 0:
        return 0
    else:
        return 1

# 异或门的实现，由其他感知机叠加而成
def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1,x2)
    y = AND(s1, s2)
    return y

# print(XOR(0, 0))
# print(XOR(0, 1))
# print(XOR(1, 0))
# print(XOR(1, 1))