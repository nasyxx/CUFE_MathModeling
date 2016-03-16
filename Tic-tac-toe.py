#!/usr/bin/env python3
"""
Tic-tac-toe
"""
__date__ = 'March 14, 2016'
__author__ = 'Nasy'

import random

board = [[0 for i in range(3)] for j in range(3)]

CHESS = [' ', '●', '○']


def show_board():
    print('    a   b   c  ')
    for i in range(3):
        print('  |---|---|---|')
        print(i + 1, '| ', end='')
        for j in range(3):
            print('%s | ' % CHESS[board[i][j]], end='')
        print()
    print('  |---|---|---|')


ROW = {'1': 0, '2': 1, '3': 2}
COL = {'a': 0, 'b': 1, 'c': 2}


def move_man():
    print('Your turn...')
    while True:
        try:
            move = input('choose a position (e.g. a1/a2/b3/c2...):\n')
            pos_row = ROW[move[1]]
            pos_col = COL[move[0]]
            if board[pos_row][pos_col] == 0:
                board[pos_row][pos_col] = 1
                return
        except KeyError:
            pass


def move_ai():
    print('AI\'s turn...')
    while True:
        r = random.randint(0, 2)
        c = random.randint(0, 2)
        if board[r][c] == 0:
            board[r][c] = 2
            return


def is_finished():
    # row
    if [1, 1, 1] in board:
        print('You win!')
        return True
    if [2, 2, 2] in board:
        print('AI wins!')
        return True
    # col
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] == 1:
            print('You win!')
            return True
        if board[0][i] == board[1][i] == board[2][i] == 2:
            print('AI wins!')
            return True
    # diagonal
        if (board[0][0] == board[1][1] == board[2][2] == 1) or (board[2][0] == board[1][1] == board[0][2] == 1):
            print('You win!')
            return True
        if (board[0][0] == board[1][1] == board[2][2] == 2) or (board[2][0] == board[1][1] == board[0][2] == 2):
            print('AI wins!')
            return True
    # draw game
    draw = True
    for j in range(3):
        if 0 in board[j]:
                draw = False
        if draw:
            print('Draw game!')
            return True
        return False

yourTurn = True

while not is_finished():
    if yourTurn:
        move_man()
    else:
        move_ai()
    show_board()
    yourTurn = not yourTurn
