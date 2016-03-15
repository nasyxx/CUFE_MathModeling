#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ヽ(。_°)ノ 这是第一个剑魔
"""

__date__ = 'March 13, 2016'
__author__ = 'Nasy'

import pylab

t = pylab.np.linspace(1, 20, 20)
k = 0.00082
p = pylab.np.zeros(20)
p[0] = 9.6
for i in range(19):
    p[i + 1] = k * (665 - p[i]) * p[i] + p[i]

pylab.scatter(t, p)
pylab.axis([0, 21, 0, 700])
pylab.show()
