#!/user/bin/env python3
# -*- coding: utf-8 -*-

from matplotlib.image import imread
import matplotlib.pyplot as plt

img = imread('91.jpg')

plt.imshow(img)
plt.show()