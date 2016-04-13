#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Solve With Pulp
@Version: 1
@Author: Nasy
@Date: April 13, 2016
@email: sy_n@me.com
@file: 0701.py
@license: MIT
"""

__version__ = '1'
__author__ = 'Nasy'
__date__ = 'April 13, 2016'
__email__ = 'sy_n@me.com'
__file__ = '0701.py'
__license__ = 'MIT'

import pulp

prop = pulp.LpProblem(sense=-1)

a = pulp.LpVariable('a', 0, cat='Integer')
b = pulp.LpVariable('b', 0, cat='Integer')

prop += 2 * a + 3 * b

prop += a + 2 * b <= 8
prop += 4 * a <= 16
prop += 4 * b <= 12

prop.solve()

for i in prop.variables():
    print(i.name + "=" + str(i.varValue))

print('max(2a + 3b) =', pulp.value(prop.objective))
