#!/usr/bin/env python
# Gomoku
# not finished yet
__date__ = 'March 15, 2016'
__author__ = 'Nasy'

board = [[0 for col in range(15)] for raw in range(15)]
CHESS = [' ', 'o', 'x']

def show_board():
    print '     A   B   C   D   E   F   G   H   I   J   K   L   M   N   O '
    for i in range(15):
        print '  ','|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|'
        if i < 9:
            print i+1, ' |',
            for j in range(15):
                print CHESS[board[i][j]], '|',
            print
        else:
            print i+1, '|',
            for j in range(15):
                print CHESS[board[i][j]], '|',
            print
    print '  ',
    print '|---'*15 + '|'
    return

show_board()