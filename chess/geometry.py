import pygame
class GameState:
    def __init__(self):
        self.board = [
            ["bR","bN","bB","bQ","bK","bB","bN","bR"],
            ["bp","bp","bp","bp","bp","bp","bp","bp"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["wp","wp","wp","wp","wp","wp","wp","wp"],
            ["wR","wN","wB","wQ","wK","wB","wN","wR"]
        ]
        self.whitetomove = True
        self.movelog = []

class king:
    pass

def draw_piece():
    pieces = ['wK','wQ','wR','wB','wN','wp','bK','bQ','bR','bB','bN','bp']
    images = {}
    for piece in pieces:
        images[piece] = pygame.image.load("images/" + piece + ".png")

def draw_text(screen,font_name,text,size,x,y,color):
    font = pygame.font.Font(font_name,size)
    text_surface = font.render(text,True,color)
    text_rect = text_surface.get_rect()
    text_rect.centerx = x
    text_rect.top = y
    screen.blit(text_surface,text_rect)

#這邊原本預計是想讓字體大小和位置可以隨著版面大小變，但參數部分還要調整
def draw_board(screen,sidelen,color1,color2,font_name):
    color = [color1,color2]
    for i in range(8):
        for j in range(8):
            pygame.draw.rect(screen,color[(i+j)%2],pygame.Rect(sidelen/8*i,sidelen/8*j,sidelen,sidelen))
    a = 0
    for i in ["a","b","c","d","e","f","g","h"]:
        draw_text(screen,font_name,i,int(sidelen/28),int(sidelen/8*(7/8 + a)),int(sidelen * 61/64),color[a%2])
        a += 1
    for i in range(1,9):
        draw_text(screen,font_name,str(9-i),int(sidelen/32),int(sidelen/64),int(4+sidelen/8*(i-1)),color[i%2])
