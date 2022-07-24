import pygame as p
import engine as e

FPS = 60
SIDELEN = 512
sl = int(SIDELEN/8)
WHITE = (255,255,255)
LIGHTGRAY = (211,211,211)

p.init()
screen = p.display.set_mode((SIDELEN,SIDELEN))
clock = p.time.Clock()
font_name = p.font.match_font("arial")
gs = e.GameState()
move = e.move()
IMAGE = {}
pieces = ['wK','wQ','wR','wB','wN','wp','bK','bQ','bR','bB','bN','bp']
for piece in pieces:
    IMAGE[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"),(sl,sl))

def draw_piece():
    for w in range(8):
        for h in range(8):
            if gs.board[h][w] != "--":
                screen.blit(IMAGE[gs.board[h][w]],p.Rect(sl*w,sl*h,sl,sl))

def main():
    running = True
    select = ()
    choosing = False
    while running:
        clock.tick(FPS)
        for event in p.event.get():
            if event.type == p.QUIT:
                running = False  
            if event.type == p.MOUSEBUTTONDOWN:
                    selecting = p.mouse.get_pos()
                    mr = selecting[1]//sl
                    mc = selecting[0]//sl
                    if not choosing and ((gs.whitetomove and gs.board[mr][mc][0] == "w") or 
                    ((not gs.whitetomove) and gs.board[mr][mc][0] == "b")):
                        select = (mr,mc)
                        move.find_allowed_moves(gs.board,gs.movelog1,mr,mc)
                        choosing = True
                    elif choosing:
                        if (mr,mc) in move.allowed_moves:
                            move.move_piece(gs.board,select[0],select[1],mr,mc)
                            move.record_move(gs.movelog1,select[0],select[1],mr,mc)
                            choosing = False
                            gs.whitetomove = not gs.whitetomove
                            move.threated_squares = [[],[]]
                            move.allowed_moves = []
                            select = ()
                            move.special_moves = [[],[],[]]
                            for i in gs.board:
                                print(i)
                            print("")
                            print(gs.movelog1)
                            print("")
                        else:
                            if gs.board[mr][mc][0] == gs.board[select[0]][select[1]][0]:
                                move.allowed_moves = []
                                move.special_moves = [[],[],[]]
                                select = (mr,mc)
                                move.find_allowed_moves(gs.board,gs.movelog1,mr,mc)
                            else:
                                choosing = False
                                select = ()
                                move.allowed_moves = []
                                move.special_moves = [[],[],[]]

        e.draw_board(screen,SIDELEN,WHITE,LIGHTGRAY,font_name)
        draw_piece()
        if choosing:
            e.move.display_allowed_move(move,screen,gs.board)
        p.display.update()
    p.quit()

if __name__ == "__main__":
    main()
