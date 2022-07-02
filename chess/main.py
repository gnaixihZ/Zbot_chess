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
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                    selecting = pygame.mouse.get_pos()
                    mr = selecting[0]//sl
                    mc = selecting[1]//sl
                    if select == (mr,mc):
                        select = ()
                        clicks = []
                    else:
                        select = (mr,mc)
                        clicks.append(select)
                    if gs.board[clicks[0][1]][clicks[0][0]] == "--":
                        select = ()
                        clicks = []
                    if len(clicks) == 2:
                        gs.board[clicks[1][1]][clicks[1][0]] = gs.board[clicks[0][1]][clicks[0][0]]
                        gs.board[clicks[0][1]][clicks[0][0]] = "--"
                        select = ()
                        clicks = []
                        for i in range(8):
                                print(gs.board[i])
        screen.fill((WHITE))
        g.draw_board(screen,SIDELEN,WHITE,LIGHTGRAY,font_name)
        draw_piece()
        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()
