#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
The 8th class
@Version: 1
@Author: Nasy
@Date: April 20, 2016
@email: sy_n@me.com
@file: m0801.py
@license: MIT
"""

import numpy as np
import plotly.offline as py
import scipy.optimize as optimize


def main():
    """
    main function
    """

    def fun(v_x, params):
        """
        function
        """
        p_a, = params
        return p_a * v_x ** 2

    def residual(params, v_x, v_y):
        """
        residual
        """
        return fun(v_x, params) - v_y

    x_i = np.array([0.5, 1.0, 1.5, 2.0, 2.5])
    y_i = np.array([0.7, 3.4, 7.2, 12.4, 20.1])

    fit_xy = optimize.leastsq(residual, [1], (x_i, y_i))
    y_i_r = fun(x_i, fit_xy[0])

    fig = dict(
        data=[
            dict(
                type='scatter',
                x=x_i,
                y=y_i_r,
                name='y = ax^2',
                line=dict(
                    shape='spline'
                )
            ),
            dict(
                type='scatter',
                x=x_i,
                y=y_i,
                name='real',
                line=dict(
                    dash='dot',
                    color='red',
                ),
                marker=dict(
                    symbol='x',
                    size=10
                ),
            )
        ],
        layout=dict(
            title='Least-square fitting test'
        )
    )
    print(fit_xy[0])
    py.plot(fig, filename='./08/m0801.html')

if __name__ == '__main__':
    main()
