import pygame
import os
import geometry as g
FPS = 60
SIDELEN = 512
WHITE = (255,255,255)
LIGHTGRAY = (211,211,211)

pygame.init()
screen = pygame.display.set_mode((SIDELEN,SIDELEN))
clock = pygame.time.Clock()
font_name = pygame.font.match_font("arial")

running = True

while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    g.draw_board(screen,SIDELEN,WHITE,LIGHTGRAY,font_name)
    pygame.display.update()
pygame.quit()
