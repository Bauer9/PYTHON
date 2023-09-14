# Creating Tetris in Python with pygame
# https://www.youtube.com/watch?v=nF_crEtmpBo

import pygame,sys
#from grid import Grid
#from blocks import *
#import blocks.
from game import Game
from colors import Colors



#BODY

pygame.init()

title_font = pygame.font.Font (None, 40)
score_surface = title_font.render ("Score", True, Colors.white )
next_surface = title_font.render ("Next", True, Colors.white)
game_over_surface = title_font.render ("GAME OVER", True, Colors.white)


score_rect = pygame.Rect (320, 55, 170, 60)
next_rect = pygame.Rect (320, 215, 170, 180)

#dark_blue = (44, 44, 127)

#screen = pygame.display.set_mode ((300, 600))

screen = pygame.display.set_mode ((500, 620))
pygame.display.set_caption("Python Tetris Mark Zero")

clock = pygame.time.Clock()

#game_grid = Grid()

#block = OBlock()
#block.move (4, 3)
#block = IBlock()

game = Game ()

GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer (GAME_UPDATE, 200)  # speed the pieces go down now "200"

"""
game_grid.grid [0] [0] = 1
game_grid.grid [3] [5] = 4
game_grid.grid [17] [8] = 7

game_grid.print_grid()

"""
#view the Blocks
#block = LBlock()
#block = JBlock()
#block = IBlock()
#block = OBlock()
#block = SBlock()
#block = TBlock()
#block = ZBlock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if game.game_over == True:
                game.game_over = False
                game.reset()
            if event.key == pygame.K_LEFT and game.game_over == False:
                game.move_left()
            if event.key == pygame.K_RIGHT and game.game_over == False:
                game.move_right()
            if event.key == pygame.K_3 and game.game_over == False:
                game.move_down()
                game.update_score (0, 1)
            if event.key == pygame.K_1 and game.game_over == False:
                game.rotate()
        if event.type == GAME_UPDATE and game.game_over == False:
            game.move_down()
            
    
    
    
    #Drawing
    score_value_surface = title_font.render(str(game.score), True, Colors.white)
    
    
    screen.fill(Colors.dark_blue)
    screen.blit(score_surface, (365, 20, 50, 50))
    screen.blit(next_surface, (375, 180, 50, 50))
    
    if game.game_over == True:
        screen.blit(game_over_surface, (320, 450, 50, 50))
    
    pygame.draw.rect (screen, Colors.light_blue, score_rect, 0, 10)
    screen.blit (score_value_surface, score_value_surface.get_rect (centerx = score_rect.centerx, centery = score_rect.centery))
    pygame.draw.rect (screen, Colors.light_blue, next_rect, 0, 10)
    game.draw (screen)
    
    
    #game_grid.draw(screen)
    #block.draw(screen)
    game.draw (screen)
    #game.move_down () #60 frames per second the pieces go down to fast, not good
    
    pygame.display.update()
    clock.tick(60)   
    
    

