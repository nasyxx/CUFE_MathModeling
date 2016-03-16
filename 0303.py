#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ヽ(。_°)ノ 这是第四个剑魔
"""
__date__ = 'March 16, 2016'
__author__ = 'Nasy'

import pylab
pylab.subplot(3, 1, 1)
t = pylab.np.linspace(1, 20, 20)
o = pylab.np.zeros(20)
h = pylab.np.zeros(20)
o[0] = 149
h[0] = 201
for i in range(19):
    o[i + 1] = 1.2 * o[i] - 0.001 * o[i] * h[i]
    h[i + 1] = 1.3 * h[i] - 0.002 * o[i] * h[i]

pylab.scatter(t, o)
pylab.scatter(t, h)

pylab.subplot(3, 1, 2)
t = pylab.np.linspace(1, 20, 20)
o = pylab.np.zeros(20)
h = pylab.np.zeros(20)
o[0] = 151
h[0] = 199
for i in range(19):
    o[i + 1] = 1.2 * o[i] - 0.001 * o[i] * h[i]
    h[i + 1] = 1.3 * h[i] - 0.002 * o[i] * h[i]

pylab.scatter(t, o)
pylab.scatter(t, h)

pylab.subplot(3, 1, 3)
t = pylab.np.linspace(1, 20, 20)
o = pylab.np.zeros(20)
h = pylab.np.zeros(20)
o[0] = 10
h[0] = 10
for i in range(19):
    o[i + 1] = 1.2 * o[i] - 0.001 * o[i] * h[i]
    h[i + 1] = 1.3 * h[i] - 0.002 * o[i] * h[i]

pylab.scatter(t, o)
pylab.scatter(t, h)

pylab.show()
