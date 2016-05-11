#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Version: 1
@Author: Nasy
@Date: May 4, 2016
@email: sy_n@me.com
@file: py1001.py
@license: MIT
"""

import numpy as np


def main():
    """
    main function
    """
    a_x = np.array([[2, 3, 1],
                    [4, 2, 3],
                    [7, 1, -1]])
    a_y = np.array([[4],
                    [17],
                    [1]])

    print(np.dot(np.linalg.inv(a_x), a_y))

if __name__ == '__main__':
    main()
