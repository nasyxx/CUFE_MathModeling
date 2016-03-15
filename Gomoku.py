#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gomoku board game
"""
# not finished yet
__date__ = 'March 15, 2016'
__author__ = 'Nasy'

board = [[0 for col in range(15)] for raw in range(15)]
CHESS = [' ', 'o', 'x']

def show_board():
    print('     A   B   C   D   E   F   G   H   I   J   K   L   M   N   O ')
    for i in range(15):
        print('  ','|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|')
        if i < 9:
            print(i+1, ' |', end='')
            for j in range(15):
                print(CHESS[board[i][j]], ' |', end='')
            print()
        else:
            print(i+1, '|', end='')
            for j in range(15):
                print(CHESS[board[i][j]], ' |', end='')
            print()
    print('   ' + '|---'*15 + '|')
    return

show_board()