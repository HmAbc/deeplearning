#!/user/bin/env python3
# -*- coding: utf-8 -*-

import numpy
from matplotlib import pyplot

x = numpy.arange(0, 6, 0.1)
y = numpy.sin(x)
y2 = numpy.cos(x)

#绘制图形
pyplot.plot(x, y, label='sin')
pyplot.plot(x, y2, lable="cos")
pyplot.xlabel('x')
pyplot.ylabel('y')
pyplot.title('sin&cos')
pyplot.legend()
pyplot.show()