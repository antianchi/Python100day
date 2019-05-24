# -*- coding: utf-8 -*-
"""
Author: antch
Email: atc00@foxmail.com

date: 2019/5/24 14:19
desc: 井字棋游戏，来源https://item.jd.com/11943853.html.
"""

import sys
import os
reload(sys)
sys.setdefaultencoding('utf8')

def print_board(board):
    print(board['TL'] + '|' + board['TM']+'|'+board['TR'])
    print("-+-+-")
    print(board['ML'] + '|' + board['MM']+'|' + board['MR'])
    print('-+-+-')
    print(board['BL']+'|'+board['BM']+'|'+board['BR'])
def main():
    init_board = {
        'TL': ' ', 'TM': ' ', 'TR': ' ',
        'ML': ' ', 'MM': ' ', 'MR': ' ',
        'BL': ' ', 'BM': ' ', 'BR': ' '
    }
    begin = True
    while begin:
        curr_board = init_board.copy()
        begin = False
        turn = 'X'
        counter = 0
        os.system('cls')
        print_board(curr_board)
        while counter < 9:
            move = input('轮到%s走棋，亲输入位置：' % turn)
            if curr_board[move] == ' ':
                counter +=1
                curr_board[move] = turn
                if turn == 'X':
                    turn = 'O'
                else:
                    turn = 'X'
            os.system('cls')
            print_board(curr_board)
        choice = input('再玩一局？yes')
        begin = choice == 'yes'
if __name__ == '__main__':
    main()
