import pygame
import geometry as g

FPS = 60
SIDELEN = 512
sl = int(SIDELEN/8)
WHITE = (255,255,255)
LIGHTGRAY = (211,211,211)

pygame.init()
screen = pygame.display.set_mode((SIDELEN,SIDELEN))
clock = pygame.time.Clock()
font_name = pygame.font.match_font("arial")
gs = g.GameState()
move = g.move()
IMAGE = {}
pieces = ['wK','wQ','wR','wB','wN','wp','bK','bQ','bR','bB','bN','bp']
for piece in pieces:
    IMAGE[piece] = pygame.transform.scale(pygame.image.load("images/" + piece + ".png"),(sl,sl))

def draw_piece():
    for w in range(8):
        for h in range(8):
            if gs.board[h][w] != "--":
                screen.blit(IMAGE[gs.board[h][w]],pygame.Rect(sl*w,sl*h,sl,sl))

def main():
    running = True
    select = ()
    clicks = []
    choosing = False
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  
            if event.type == pygame.MOUSEBUTTONDOWN:
                    selecting = pygame.mouse.get_pos()
                    mr = selecting[1]//sl
                    mc = selecting[0]//sl
                    if select == (mr,mc):
                        select = ()
                        clicks = []
                        move.allowed_moves = []
                        choosing = False
                    else:
                        choosing = True
                        select = (mr,mc)
                        clicks.append(select)
                        move.movable(gs.board,mr,mc)
                        if move.allowed_moves == []:
                            select = ()
                            clicks = []
                            choosing = False
                    if len(clicks) == 1:
                        if gs.board[clicks[0][0]][clicks[0][1]] == "--" or (gs.whitetomove and gs.board[clicks[0][0]][clicks[0][1]][0] == "b") or ((not gs.whitetomove) and gs.board[clicks[0][0]][clicks[0][1]][0] == "w"):
                            select = ()
                            clicks = []
                            move.allowed_moves = []
                            choosing = False
                    if len(clicks) == 2:
                        if clicks[1] in move.allowed_moves:
                            gs.board[clicks[1][0]][clicks[1][1]] = gs.board[clicks[0][0]][clicks[0][1]]
                            gs.board[clicks[0][0]][clicks[0][1]] = "--"
                            for i in range(8):
                                print(gs.board[i])
                            select = ()
                            clicks = []
                            choosing = False
                            gs.whitetomove = not gs.whitetomove
                            move.allowed_moves = []
                        else:
                            clicks = []
                            move.allowed_moves = []
                            choosing = True
                            select = (mr,mc)
                            clicks.append(select)
                            move.movable(gs.board,mr,mc)
        g.draw_board(screen,SIDELEN,WHITE,LIGHTGRAY,font_name)
        draw_piece()
        if choosing:
            g.move.display_move(move,screen,gs.board)
        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()
