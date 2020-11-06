#!/user/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

def softmax(x):
    c = np.max(x)
    exp_a = np.exp(x - c)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a

    return y

a = np.array([0.3, 2.9, 4])
y = softmax(a)
print(y)