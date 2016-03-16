#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ヽ(。_°)ノ 这是第三个剑魔
"""
__date__ = 'March 16, 2016'
__author__ = 'Nasy'

import pylab
t = pylab.np.linspace(1, 9, 9)
x = pylab.np.zeros(9)
y = pylab.np.zeros(9)
x[0] = 7000
y[0] = 0

for i in range(8):
    x[i + 1] = 0.6 * x[i] + 0.3 * y[i]
    y[i + 1] = 0.4 * x[i] + 0.7 * y[i]

pylab.scatter(t, x)
pylab.scatter(t, y)

pylab.show()
