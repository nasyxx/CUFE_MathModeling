#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ヽ(。_°)ノ 这是第五个剑魔
"""
__date__ = 'March 23, 2016'
__author__ = 'Nasy'

import plotly.offline as py
import plotly.graph_objs as go
import numpy as np

x = np.linspace(20, 40, 5)
y = np.array([20, 28, 40.5, 52.5, 72])

y1 = np.array([18, 25, 36, 47, 64])
y2 = np.array([22, 31, 45, 58, 80])

ey1 = y - y1
ey2 = y2 - y

data = [
    go.Scatter(
        x=x,
        y=y,

        error_y=dict(
            array=ey1,
            arrayminus=ey2
        )
    )
]

py.plot(data, filename='0401 with plotly')
