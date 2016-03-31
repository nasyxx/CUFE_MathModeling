#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ヽ(。_°)ノ 这是 plotly 测试
"""

__author__ = "Nasy"
__date__ = "March 30, 2016"

import plotly.offline as pyo
import plotly.graph_objs as go

trace0 = go.Scatter(
    x=[1, 2, 3, 4],
    y=[10, 15, 13, 17]
)
trace1 = go.Scatter(
    x=[1, 2, 3, 4],
    y=[16, 5, 11, 9]
)
data = [trace0, trace1]
pyo.plot(data, filename='plot test 01.html')
