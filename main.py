# libraries import
import pygame
import random
import time

# game function import
from blocks import base_blocks
from functions import game
pygame.init()


# variables
game_functions = game()

run = True
witdh = 1000
height = 800
speed = 1

block_size = (witdh-600) // 10
board = [[0] * 10 for _ in range(20)]
colors = ["#00FFEF", "#0011FF", "#FF6F00", "#F7FF00", "#1AFF00", "#B300FF", "#FF0000"]

curr_color = random.choice(colors)
active = game_functions.create_new()


# pygame functions
move_down = pygame.USEREVENT
pygame.time.set_timer(move_down, 100)


# window
screen = pygame.display.set_mode((witdh, height))
screen.fill((255,255,255))



# game area
game_screen = pygame.Surface((400, height))
game_screen.fill((255,255,255))



# side panels
pygame.draw.rect(screen, pygame.Color("#4A4A4A"), pygame.Rect(0, 0, 290, height))
pygame.draw.rect(screen, (0,0,0), pygame.Rect(290, 0, 10, height))

pygame.draw.rect(screen, pygame.Color("#4A4A4A"), pygame.Rect(witdh-290, 0, 290, height))
pygame.draw.rect(screen, (0,0,0), pygame.Rect(witdh-300, 0, 10, height))


# functions
def update_game():
    pygame.Surface.blit(screen, game_screen, (300, 0))
    pygame.display.update()

def create_new_block():
    curr_color = random.choice(colors)
    active = game_functions.create_new()

    return curr_color, active

def into_board(active):
    for y, x in active:
        board[y][x] = 1


def draw_board(board):
    for y in range(0, len(board)):
        for x in range(0, len(board[0])):
            if board[y][x] == 1:
                pygame.draw.rect(game_screen, pygame.Color(curr_color), pygame.Rect(x*block_size, y*block_size, block_size, block_size))


def delete(pos):
    for y, x in pos:
        board[y][x] = 0
        pygame.draw.rect(game_screen, (255,255,255), pygame.Rect(x*block_size, y*block_size, block_size, block_size))

def check_end(active):
    for y, x in active:
        if board[y][x] == 1:
            return True
    return False












into_board(active)
draw_board(board)
update_game()

pygame.time.set_timer(move_down, 100)
while run:
    for event in pygame.event.get():

        if event.type == move_down:
            flag = game_functions.move_down(board, active)

            if flag == True:
                delete(active)
                active = [[y+1, x] for y, x in active]
            else:
                curr_color, active = create_new_block()

                if check_end(active) == True:
                    run = False
                
            into_board(active)
            draw_board(board)
            update_game()




        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False


            if event.key == pygame.K_LEFT:
                flag = game_functions.move_left(board, active)

                if flag == True:
                    delete(active)
                    active = [[y, x-1] for y, x in active]

                    into_board(active)
                    draw_board(board)
                    update_game()

            if event.key == pygame.K_RIGHT:
                flag = game_functions.move_right(board, active)

                if flag == True:
                    delete(active)
                    active = [[y, x+1] for y, x in active]

                    into_board(active)
                    draw_board(board)
                    update_game()


pygame.quit()