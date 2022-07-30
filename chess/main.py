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

PIMAGE = {}
ppieces = ['wQ','wR','wB','wN','bQ','bR','bB','bN']
for ppiece in ppieces:
    PIMAGE[ppiece] = p.transform.scale(p.image.load("images/" + ppiece + ".png"),(96,96))

def promotion(board,sr,sc,er,ec):
    x = 0
    for i in ["Q","R","B","N"]:
        screen.blit(PIMAGE[board[sr][sc][0]+i],p.Rect(16 + x * 128,208,96,96))
        x += 1
    p.display.update()
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in p.event.get():
            if event.type == p.QUIT:
                p.quit()
                return True
            if event.type == p.MOUSEBUTTONDOWN:
                sellecting = p.mouse.get_pos()
                mx = sellecting[0]
                my = sellecting[1]
                x = 0
                for i in ["Q","R","B","N"]:
                    if my in range(208,305) and mx in range(16 + x * 128,113 + x * 128):
                        board[er][ec] =  board[sr][sc][0] + i
                        board[sr][sc] = "--"
                        print(board[er][ec])
                        move.promotion = False
                        return False
                    x += 1

def main():
    running = True
    choosing = False
    sellect = ()
    while running:
        clock.tick(FPS)
        for event in p.event.get():
            if event.type == p.QUIT:
                running = False  
            if event.type == p.MOUSEBUTTONDOWN:
                    sellecting = p.mouse.get_pos()
                    mr = sellecting[1]//sl
                    mc = sellecting[0]//sl
                    if not choosing and ((gs.whitetomove and gs.board[mr][mc][0] == "w") or 
                    ((not gs.whitetomove) and gs.board[mr][mc][0] == "b")):
                        sellect = (mr,mc)
                        move.find_allowed_moves(gs.board,gs.movelog1,mr,mc)
                        choosing = True
                    elif choosing:
                        if (mr,mc) in move.allowed_moves:
                            move.move_piece(gs.board,sellect[0],sellect[1],mr,mc)
                            if move.promotion:
                                close = promotion(gs.board,sellect[0],sellect[1],mr,mc)
                                if close:
                                    break
                            move.record_move(gs.movelog1,sellect[0],sellect[1],mr,mc)
                            choosing = False
                            gs.whitetomove = not gs.whitetomove
                            move.allowed_moves = []
                            sellect = ()
                            move.special_moves = [[],[],[]]
                            for i in gs.board:
                                print(i)
                            print("")
                            print(gs.movelog1)
                            print("")
                            if gs.whitetomove:
                                color = 0
                            else:
                                color = 1
                            if move.test_game_over(gs.board,gs.movelog1,color):
                                if move.isthreated(gs.board,gs.movelog1,move.wk[0][0],move.wk[0][1]):
                                    print("Black Won!!!")
                                elif move.isthreated(gs.board,gs.movelog1,move.bk[0][0],move.bk[0][1]):
                                    print("White Won!!!")
                                else:
                                    print("Stalemate")
                        else:
                            if gs.board[mr][mc][0] == gs.board[sellect[0]][sellect[1]][0]:
                                move.allowed_moves = []
                                move.special_moves = [[],[],[]]
                                sellect = (mr,mc)
                                move.find_allowed_moves(gs.board,gs.movelog1,mr,mc)
                            else:
                                choosing = False
                                sellect = ()
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
