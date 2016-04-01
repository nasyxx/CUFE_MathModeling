#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ヽ(。_°)ノ 这是第一个剑魔 plotly 版本
"""

__date__ = 'April 1, 2016'
__author__ = 'Nasy'

import plotly.offline as py
import plotly.graph_objs as go
import numpy as np

t = np.linspace(1, 20, 20)
k = 0.00082
p = np.zeros(20)
p[0] = 9.6
for i in range(19):
    p[i + 1] = k * (665 - p[i]) * p[i] + p[i]

figure = go.Figure(
    data=[
        go.Scatter(
            x=t,
            y=p,
            mode='markers',
            name='0201~'
        )
    ],
    layout=go.Layout(
        title='0201'
    )
)

py.plot(figure, filename='0201 with plotly.html')
