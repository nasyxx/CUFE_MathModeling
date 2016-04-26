#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Solve With Pulp
@Version: 1
@Author: Nasy
@Date: April 13, 2016
@email: sy_n@me.com
@file: p0701.py
@license: MIT
"""

import pulp


def main():
    """
    main function
    """
    prop = pulp.LpProblem(sense=-1)

    var_x = pulp.LpVariable('x', 0, cat='Integer')
    var_y = pulp.LpVariable('y', 0, cat='Integer')

    prop += 2 * var_x + 3 * var_y

    prop += var_x + 2 * var_y <= 8
    prop += 4 * var_x <= 16
    prop += 4 * var_y <= 12

    prop.solve()

    for i in prop.variables():
        print(i.name + "=" + str(i.varValue))

    print('max(2a + 3b) =', pulp.value(prop.objective))

if __name__ == '__main__':
    main()
