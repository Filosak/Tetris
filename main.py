# libraries import
import pygame
import random
import time

# game function import
from blocks import base_blocks
from functions import game
pygame.init()
pygame.font.init()


# variables
game_functions = game()
font = pygame.font.Font("project/fonts/Futura_black.ttf", 45)
font_inside_block = pygame.font.Font("project/fonts/Futura_black.ttf", 55)

run = True
witdh = 1000
height = 800
speed = 1
curr_top_y = 0
curr_top_x = 4

score = 0
level = 0
rows = 20

block_size = (witdh-600) // 10
board = [[0] * 10 for _ in range(20)]
colors = ["#00FFEF", "#0011FF", "#FF6F00", "#F7FF00", "#1AFF00", "#B300FF", "#FF0000"]

curr_color = random.choice(colors)
active = game_functions.create_new()

next_color = random.choice(colors)
next_active = game_functions.create_new()


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


# 
# right side (next, score, level, rows)
#

# next block
pygame.draw.rect(screen, (0,0,0), pygame.Rect(witdh-255, 45, 210, 210))

# next block surface
next_screen = pygame.Surface((200, 200))
next_screen.fill((255,255,255))

# next block text
text_surface = font.render('Next', False, (0, 0, 0))
screen.blit(text_surface, (witdh-205, 5, 210, 210))


# score block
pygame.draw.rect(screen, (0,0,0), pygame.Rect(witdh-270, 355, 250, 85))

# score surface
score_screen = pygame.Surface((240, 75))
score_screen.fill((255,255,255))


# score text
text_surface = font.render('Score', False, (0, 0, 0))
screen.blit(text_surface, (witdh-220, 310, 210, 210))


# level block
pygame.draw.rect(screen, (0,0,0), pygame.Rect(witdh-270, 500, 250, 85))

# level surface
level_screen = pygame.Surface((240, 75))
level_screen.fill((255,255,255))

# level text
text_surface = font.render('Level', False, (0, 0, 0))
screen.blit(text_surface, (witdh-215, 460, 210, 210))


# rows block
pygame.draw.rect(screen, (0,0,0), pygame.Rect(witdh-270, 650, 250, 85))

# rows surface
rows_screen = pygame.Surface((240, 75))
rows_screen.fill((255,255,255))

# rows text
text_surface = font.render('Rows', False, (0, 0, 0))
screen.blit(text_surface, (witdh-215, 610, 210, 210))


# left side (hold)
pygame.draw.rect(screen, (0,0,0), pygame.Rect(50, 45, 210, 210))
pygame.draw.rect(screen, (255,255,255), pygame.Rect(55, 50, 200, 200))

text_surface = font.render('Hold', False, (0, 0, 0))
screen.blit(text_surface, (100, 5, 210, 210))




# functions
def update_game():
    pygame.Surface.blit(screen, next_screen, (witdh-250, 50))
    pygame.Surface.blit(screen, score_screen, (witdh-265, 360))
    pygame.Surface.blit(screen, level_screen, (witdh-265, 505))
    pygame.Surface.blit(screen, rows_screen, (witdh-265, 655))
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
    game_screen.fill((255,255,255))
    
    for y in range(0, len(board)):
        for x in range(0, len(board[0])):
            if board[y][x] == 1:
                pygame.draw.rect(game_screen, pygame.Color(curr_color), pygame.Rect(x*block_size, y*block_size, block_size, block_size))


def delete(pos):
    for y, x in pos:
        board[y][x] = 0


def check_end(active):
    for y, x in active:
        if board[y][x] == 1:
            return True
    return False

def draw_next(next_block, next_color):
    next_screen.fill((255,255,255))

    lb = len(next_block)
    lbi = len(next_block[0])

    for y in range(0, lb):
        for x in range(0, lbi):
            if next_block[y][x] == 1:
                pygame.draw.rect(next_screen, pygame.Color(next_color), pygame.Rect((x+1)*block_size, (y+1)*block_size, block_size, block_size))


def draw_stats(score, level, rows):
    score_screen.fill((255,255,255))
    level_screen.fill((255,255,255))
    rows_screen.fill((255,255,255))

    score_text_surface = font.render(str(score), False, (0, 0, 0))
    level_text_surface = font.render(str(level), False, (0, 0, 0))
    rows_text_surface = font.render(str(rows), False, (0, 0, 0))

    score_screen.blit(score_text_surface, (5, 5))
    level_screen.blit(level_text_surface, (5, 5))
    rows_screen.blit(rows_text_surface, (5, 5))



# initial drawing
into_board(active)
draw_board(board)
draw_next(game_functions.next_curr_block, next_color)
update_game()
pygame.time.set_timer(move_down, 200)


# game loop
while run:
    for event in pygame.event.get():

        if event.type == move_down or (event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN):
            flag = game_functions.move_down(board, active)

            if flag == True:
                delete(active)
                active = [[y+1, x] for y, x in active]
                curr_top_y += 1
            else:
                score, level, rows = game_functions.update_stats(score, level, rows, game_functions.clear_row(board))
                draw_stats(score, level, rows)

                active, curr_color = next_active, next_color
                next_color, next_active = create_new_block()
                curr_top_y = 0
                curr_top_x = 4

                draw_next(game_functions.next_curr_block, next_color)

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
                    curr_top_x -= 1

                    into_board(active)
                    draw_board(board)
                    update_game()
                    

            if event.key == pygame.K_RIGHT:
                flag = game_functions.move_right(board, active)

                if flag == True:
                    delete(active)

                    active = [[y, x+1] for y, x in active]
                    curr_top_x += 1

                    into_board(active)
                    draw_board(board)
                    update_game()

            if event.key == pygame.K_UP:
                flag = game_functions.rotate(board, curr_top_y, curr_top_x, active)

                if flag == True:
                    delete(active)

                    active = []
                    base = game_functions.curr_block
                    lm = len(base)

                    for y in range(0, lm):
                        for x in range(0, len(base[0])):
                            if base[y][x] == 1:
                                c_y = y+curr_top_y
                                c_x = x+curr_top_x

                                active.append([c_y, c_x])
                    
                    into_board(active)
                    draw_board(board)
                    update_game()


pygame.quit()