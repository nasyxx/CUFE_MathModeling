#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ヽ(。_°)ノ 这是第五个剑魔
"""
__date__ = 'March 23, 2016'
__author__ = 'Nasy'

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(20, 40, 5)
y = np.array([20, 28, 40.5, 52.5, 72])

y1 = np.array([18, 25, 36, 47, 64])
y2 = np.array([22, 31, 45, 58, 80])

plt.errorbar(x, y, [y - y1, y2 - y], ecolor='red', color='black')
plt.xlim([15, 45])
plt.show()
