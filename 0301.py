#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ヽ(。_°)ノ 这是第二个剑魔
"""
__date__ = 'March 16, 2016'
__author__ = 'Nasy'

import pylab

t = pylab.np.linspace(1, 200, 200)
a = pylab.np.zeros(200)


pylab.subplot(3, 2, 1)
a[0] = 0.1
print()
r = 1.546
for i in range(199):
    a[i + 1] = r * a[i] * (1 - a[i])
pylab.scatter(t, a, c='black')
pylab.xlim(0, 100)
pylab.xlabel('Stage n, r = 1.546')
pylab.ylabel('Population')

pylab.subplot(3, 2, 2)
a[0] = 0.1
r = 2.750
for i in range(199):
    a[i + 1] = r * a[i] * (1 - a[i])
pylab.scatter(t, a, c='black')
pylab.xlim(0, 100)
pylab.xlabel('Stage n, r = 2.750')
pylab.ylabel('Population')

pylab.subplot(3, 2, 3)
a[0] = 0.1
r = 3.250
for i in range(199):
    a[i + 1] = r * a[i] * (1 - a[i])
pylab.scatter(t, a, c='black')
pylab.xlim(0, 100)
pylab.xlabel('Stage n, r = 3.250')
pylab.ylabel('Population')

pylab.subplot(3, 2, 4)
a[0] = 0.1
r = 3.525
for i in range(199):
    a[i + 1] = r * a[i] * (1 - a[i])
pylab.scatter(t, a, c='black')
pylab.xlim(0, 200)
pylab.xlabel('Stage n, r = 3.525')
pylab.ylabel('Population')

pylab.subplot(3, 2, 5)
a[0] = 0.1
r = 3.555
for i in range(199):
    a[i + 1] = r * a[i] * (1 - a[i])
pylab.scatter(t, a, c='black')
pylab.xlim(0, 200)
pylab.xlabel('Stage n, r = 3.555')
pylab.ylabel('Population')

pylab.subplot(3, 2, 6)
a[0] = 0.1
r = 4
for i in range(199):
    a[i + 1] = r * a[i] * (1 - a[i])
pylab.scatter(t, a, c='black')
pylab.xlim(0, 200)
pylab.xlabel('Stage n, r = 3.750')
pylab.ylabel('Population')

pylab.show()
