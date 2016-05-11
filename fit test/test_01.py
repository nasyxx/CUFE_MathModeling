#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Version: 1
@Author: Nasy
@Date: April 08, 2016
@email: sy_n@me.com
@file: test_01.py
@license: MIT
"""


import numpy as np
import plotly.graph_objs as go
import plotly.offline as py
import scipy.optimize as optimize


def main():
    """
    Main function
    """
    x_r = np.linspace(1, 16, 16)
    y_r = np.array([4, 6.4, 8, 8.8, 9.22, 9.5, 9.7, 9.86,
                    10, 10.2, 10.32, 10.42, 10.5, 10.55, 10.58, 10.6])

    def f(x, p):
        a, b, c, d = p
        return a * x ** 3 + b * x * x + c * x + d

    def residuals(p, x, y):
        return f(x, p) - y

    fit_xy = optimize.leastsq(residuals, [1, 0, 0, 0], (x_r, y_r))
    y_f = f(x_r, fit_xy[0])
    print(fit_xy[0])
    y_f2 = np.polyfit(x_r, y_r, 3)

    yy = f(x_r, y_f2)
    print(y_f2)

    fig = go.Figure(
        data=[
            go.Scatter(
                x=x_r,
                y=y_f,
                name='fit data',
                line=dict(
                    shape='spline'
                )

            ),

            go.Scatter(
                x=x_r,
                y=yy,
                name='fit data 2',
                line=dict(
                    shape='spline',
                    dash='dash'
                )

            ),

            go.Scatter(
                x=x_r,
                y=y_r,
                name='real data',
                line=dict(
                    dash='dot',
                    color='red'
                ),
                marker=dict(
                    symbol='x',
                    size=10
                )
            )

        ],
        layout=go.Layout(
            title='Least-square fitting test'
        )
    )

    py.plot(fig, filename='test 01.html')

if __name__ == '__main__':
    print('start\n')
    main()
    print('finished\n')
