#!/user/bin/env python3
# -*- coding: utf-8 -*-

import sys, os
sys.path.append(os.pardir)
from dataset.mnist import load_mnist
from PIL import Image

def show_img(img):
    pil_image = Image.fromarray(img)
    pil_image.show()

(x_train, t_train), (x_test, t_test) = load_mnist(normalize=False, flatten=True)
img = x_train[0]
label = t_train[0]
print(label)

print(img.shape)
img = img.reshape(28, 28)
print(img.shape)

show_img(img)