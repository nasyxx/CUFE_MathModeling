#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Version: 1
@Author: Nasy
@Date: May 18, 2016
@email: sy_n@me.com
@file: py01.py
@license: MIT
"""
import numpy as np
import pandas as pd
import statsmodels.api as sm


def get_data():
    """
    get data
    """
    data = pd.read_csv('./data.csv')
    data.colums = ['id', 'x1', 'x2', 'x3', 'y']
    return data


def sigmod(v_x):
    """
    sigmod function
    """
    return 1 / (1 + np.exp(v_x))


def main():
    """
    main function
    """
    data = get_data()
    train_cols = data.columns[1:]
    logit = sm.Logit(data['id'], data[train_cols])
    result = logit.fit()
    print(result.summary())

if __name__ == '__main__':
    main()
