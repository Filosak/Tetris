import random
from blocks import base_blocks
import pygame

class game:
    def __init__(self):
        self.curr_block = None
        self.next_curr_block = None

    def create_new(self):
        curr_block = random.choice(base_blocks)
        active = []

        for y in range(0, len(curr_block)):
            for x in range(0, len(curr_block[0])):
                if curr_block[y][x] == 1:
                    active.append([y, x+4])
        
        if self.curr_block == None:
            self.curr_block = curr_block
        elif self.next_curr_block == None:
            self.next_curr_block = curr_block
        else:
            self.curr_block = [row[:] for row in self.next_curr_block]
            self.next_curr_block = curr_block

        return active
        

    def move_down(self, board, active):
        for y, x in active:
            if [y+1, x] in active:
                continue
            elif y == 19 or board[y+1][x] == 1:
                return False
    
        return True

    
    def move_left(self, board, active):
        for y, x in active:
            if [y, x-1] in active:
                continue
            elif x == 0 or board[y][x-1] == 1:
                return False
        return True


    def move_right(self, board, active):
        for y, x in active:
            if [y, x+1] in active:
                continue
            elif x == 9 or board[y][x+1] == 1:
                return False
        return True


    def rotate(self, board, curr_y, curr_x, active):
        base = [row[:] for row in self.curr_block]
        lm = len(base)

        for i in range(0, lm // 2):
            for j in range(i, lm-i-1):
                base[i][j], base[j][-1-i], base[-1-i][-1-j], base[-1-j][i] = base[-1-j][i], base[i][j], base[j][-1-i], base[-1-i][-1-j]


        for y in range(0, lm):
            for x in range(0, len(base[0])):
                if base[y][x] == 1:
                    c_y = y+curr_y
                    c_x = x+curr_x

                    if c_y < 0 or c_x < 0 or c_y > 19 or c_x > 9:
                        return False
                    elif [c_y, c_x] in active:
                        continue
                    elif board[c_y][c_x] == 1:
                        return False

        self.curr_block = base
        return True


    def clear_row(self, board):
        cleared = 0

        for i in range(0, len(board)):
            if 0 not in board[i]:
                cleared += 1
                for j in range(i, 0, -1):
                    board[j] = board[j-1][:]
        
        return cleared


    def update_stats(self, score, level, rows, cleared):
        rows -= cleared

        if rows <= 0:
            level += 1
            rows = level * 10 + 20 - abs(rows)
        
        score += 100 * cleared

        return score, level, rows