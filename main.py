import pygame

from pygame.locals import *
from sys import exit

pygame.init()  #inicializar todos los modulos de pygame
pygame.font.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')

PADDLE_WIDTH = 20
PADDLE_HEIGHT = 100
left_directions = {K_a: (0, 10), K_q: (0, -10)}
right_directions = {K_UP: (0, -10), K_DOWN: (0, 10)}

def move(rect, direction):
    a = 1
    pass


clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)
sky_surface = pygame.image.load('graphics/Sky.png')
ground_surface = pygame.image.load('graphics/ground.png')
left_paddle = pygame.rect.Rect(0,0,PADDLE_WIDTH, PADDLE_HEIGHT)
right_paddle = pygame.rect.Rect(800 - PADDLE_WIDTH, 0, PADDLE_WIDTH, PADDLE_HEIGHT)
text_surface = test_font.render("My game",  False, 'Green')

pos_x_circle = 400
pos_y_circle = 250
pos_x_rect = 550
pos_y_rect = 50
update_x = 1
update_y = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key in left_directions:
                move(left_paddle, event.key)
            if event.key in right_directions:
                move(right_directions, event.key)
    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface,  (300, 50))
    

    l = pygame.draw.line(screen, (255, 0, 0), (50, 50), (150, 150), 3)
    r = pygame.draw.rect(screen, (0, 255, 255), (pos_x_rect, pos_y_rect, 100, 100))
    c = pygame.draw.circle(screen, (255, 255, 255), (pos_x_circle, pos_y_circle), 10, 10)
    e = pygame.draw.ellipse(screen, (0, 255, 0), (75, 225, 150, 100))
    
    if pos_x_circle == 800:
        update_x = -1 
    if pos_x_circle == 0:
        update_x = 1
    if pos_y_circle == 400:
        update_y = -1
    if pos_y_circle == 0:
        update_y = 1

    pos_x_circle = pos_x_circle + update_x
    pos_y_circle = pos_y_circle + update_y
    pos_x_rect += update_x*1.5
    pos_y_rect += update_y*0.3
    print(f'({pos_x_circle}, {pos_y_circle})')
    pygame.draw.rect(screen, 'Black', left_paddle)
    pygame.draw.rect(screen, 'Black', right_paddle)
    pygame.display.update()
    clock.tick(60)