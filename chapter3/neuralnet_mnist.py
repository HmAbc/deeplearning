#!/user/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import sys, os
sys.path.append(os.pardir)
import pickle
from dataset.mnist import load_mnist

def get_data():
    (x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, flatten=True, one_hot_label=False)
    return x_test, t_test

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def softmax(x):
    c = np.max(x)
    exp_a = np.exp(x - c)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y

def init_network():
    with open("sample_weight.pkl", 'rb') as f:
        network = pickle.load(f)
    return network

def predit(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']
    a1 = x @ W1 + b1
    z1 = sigmoid(a1)
    a2 = z1 @ W2 + b2
    z2 = sigmoid(a2)
    a3 = z2 @ W3 + b3
    y = softmax(a3)
    return y

x, t = get_data()
network = init_network()

accuracy_cnt = 0
for i in range(len(x)):
    y = predit(network, x[i])
    p = np.argmax(y)        # 获取最高概率元素的索引
    if p == t[i]:
        accuracy_cnt = accuracy_cnt + 1

print("accuracy: " + str(float(accuracy_cnt) / len(x)))