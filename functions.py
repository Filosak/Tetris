import random
from blocks import base_blocks
import pygame

class game:
    def __init__(self):
        self.curr_block = None

    def create_new(self):
        curr_block = random.choice(base_blocks)
        active = []

        for y in range(0, len(curr_block)):
            for x in range(0, len(curr_block[0])):
                if curr_block[y][x] == 1:
                    active.append([y, x+4])
        
        self.curr_block = curr_block
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

    def rotate(self, board, active):
        pass