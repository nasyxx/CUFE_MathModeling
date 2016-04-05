#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Version: 1
@Author: Nasy
@Date: April 01, 2016
@email: sy_n@me.com
@file: 0201 with plotly.py
@license: MIT
"""

__version__ = '1'
__author__ = 'Nasy'
__date__ = 'April 01, 2016'
__email__ = 'sy_n@me.com'
__file__ = '0201 with plotly.py'
__license__ = 'MIT'

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
