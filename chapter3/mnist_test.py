#!/user/bin/env python3
# -*- coding: utf-8 -*-

import sys, os
sys.path.append(os.pardir)  #为了导入父目录中的文件而进行的设置
from dataset.mnist import load_mnist

# 第一次调用会花费几分钟
(x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=False)

# 输出各数据的形状
print(x_train.shape)
print(t_train.shape)
print(x_test.shape)
print(t_test.shape)