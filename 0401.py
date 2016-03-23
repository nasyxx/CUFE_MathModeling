#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ヽ(。_°)ノ 这是第五个剑魔
"""
__date__ = 'March 23, 2016'
__author__ = 'Nasy'

import pylab

x = pylab.np.linspace(20, 40, 5)

y = [20, 28, 40.5, 52.5, 72]

# y1 = [2, 3, 4.5, 5.5, 8]

# y2 = [2, 3, 4.5, 5.5, 8]

y1 = [18, 25, 36, 47, 64]

y2 = [22, 31, 45, 58, 80]

for i in range(5):
    y1[i] = y[i] - y1[i]
    y2[i] = y2[i] - y[i]

pylab.errorbar(x, y, [y1, y2],ecolor='red',color='black')
pylab.xlim([15, 45])
pylab.show()
