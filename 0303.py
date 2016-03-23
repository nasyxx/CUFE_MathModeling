#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ヽ(。_°)ノ 这是第四个剑魔
"""
__date__ = 'March 16, 2016'
__author__ = 'Nasy'

import matplotlib.pyplot as plt
import numpy as np

plt.subplot(3, 1, 1)
t = np.linspace(1, 20, 20)
o = np.zeros(20)
h = np.zeros(20)
o[0] = 149
h[0] = 201
for i in range(19):
    o[i + 1] = 1.2 * o[i] - 0.001 * o[i] * h[i]
    h[i + 1] = 1.3 * h[i] - 0.002 * o[i] * h[i]

plt.scatter(t, o)
plt.scatter(t, h)

plt.subplot(3, 1, 2)
t = np.linspace(1, 20, 20)
o = np.zeros(20)
h = np.zeros(20)
o[0] = 151
h[0] = 199
for i in range(19):
    o[i + 1] = 1.2 * o[i] - 0.001 * o[i] * h[i]
    h[i + 1] = 1.3 * h[i] - 0.002 * o[i] * h[i]

plt.scatter(t, o)
plt.scatter(t, h)

plt.subplot(3, 1, 3)
t = np.linspace(1, 20, 20)
o = np.zeros(20)
h = np.zeros(20)
o[0] = 10
h[0] = 10
for i in range(19):
    o[i + 1] = 1.2 * o[i] - 0.001 * o[i] * h[i]
    h[i + 1] = 1.3 * h[i] - 0.002 * o[i] * h[i]

plt.scatter(t, o)
plt.scatter(t, h)

plt.show()
