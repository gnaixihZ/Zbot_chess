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

class move:
    def __init__(self,board,start,end):
        self.board = board
        self.sr = start[0]
        self.sc = start[1]
        self.er = end[0]
        self.ec = end[1]
        self.allowed_moves = []

#     def movable(self):
#         if self.board[self.sr][self.sc] == "--":
#             return False
#         if self.board[self.sr][self.sc] == "wp":
#             if self.er == self.sr - 1 and self.ec == self.sc and self.board[self.er][self.ec] == "--":
#                 return True
#             elif self.board[self.er][self.ec][0] == "b" and self.er == self.sr - 1 and (self.ec == self.sc + 1 or self.ec == self - 1):
#                 return True
#             else:
#                 return False
#         if self.board[start[0]][start[1]] == "wR":
#             if

#         else:
#             return True
#這邊還沒試過，反正就先寫著
    def display_move(self,screen,board,sr,sc):
        if board[sr][sc] == "--":
            return 1
        if board[sr][sc] == "wp":
            if sr == 6 and board[sr - 1][sc] == "--" and board[sr-2][sc] == "--":
                for i in [-1,-2]:
                    self.allowed_moves.append((sr + i,sc,0))
            elif sr - 1 >= 0 and board[sr - 1][sc] == "--":
                self.allowed_moves.append((sr - 1,sc,0))
            for i in [-1,1]:
                if sc + i in range(8) and board[sr - 1][sc + i][0] == "b":
                    self.allowed_moves.append((sr - 1,sc + i,1))
        if board[sr][sc] == "wR":
            for pm in [-1,1]:
                for i in range(1,8):
                    if sr + pm * i in range(8):
                        if board[sr + pm * i][sc] == "--":
                            self.allowed_moves.append((sr + pm * i,sc,0))
                        if board[sr + pm * i][sc][0] == "b":
                            self.allowed_moves.append((sr + pm * i,sc,1))
                            break
                for i in range(1,8):
                    if sc + pm * i in range(8):
                        if board[sr][sc + pm * i] == "--":
                            self.allowed_moves.append((sr,sc + pm * i,0))
                        if board[sr][sc + pm * i] == "b":
                            self.allowed_moves.append((sr,sc + pm * i,1))
                            break
        if board[sr][sc] == "wB":
            for pm in [-1,1]:
                for mp in [-1,1]:
                    for i in range(8):
                        if sr + pm * i in range(8) and sc + mp * i in range(8):
                            if board[sr + pm * i][sc + mp * i] == "--":
                                self.allowed_moves.append((sr + pm * i,sc + mp * i,0))
                            if board[sr + pm * i][sc + mp * i][0] == "b":
                                self.allowed_moves.append((sr + pm * i,sc + mp * i,1))
                                break
        if board[sr][sc] == "wN":
            for m in [[1,2],[2,1]]:
                for pm in [-1,1]:
                    for mp in [-1,1]:
                        if sr + m[0] * pm in range(8) and sc + m[1] * mp in range(8):
                            if board[sr + m[0] * pm][sc + m[1] * mp] == "--":
                                self.allowed_moves.append((sr + m[0] * pm,sc + m[1] * mp,0))
                            if board[sr + m[0] * pm][sc + m[1] * mp][0] == "b":
                                self.allowed_moves.append((sr + m[0] * pm,sc + m[1] * mp,1))
        if board[sr][sc] == "wQ":
            for pm in [-1,1]:
                for i in range(1,8):
                    if sr + pm * i in range(8):
                        if board[sr + pm * i][sc] == "--":
                            self.allowed_moves.append((sr + pm * i,sc,0))
                        if board[sr + pm * i][sc][0] == "b":
                            self.allowed_moves.append((sr + pm * i,sc,1))
                            break
                for i in range(1,8):
                    if sc + pm * i in range(8):
                        if board[sr][sc + pm * i] == "--":
                            self.allowed_moves.append((sr,sc + pm * i,0))
                        if board[sr][sc + pm * i] == "b":
                            self.allowed_moves.append((sr,sc + pm * i,1))
                            break
            for pm in [-1,1]:
                for mp in [-1,1]:
                    for i in range(8):
                        if sr + pm * i in range(8) and sc + mp * i in range(8):
                            if board[sr + pm * i][sc + mp * i] == "--":
                                self.allowed_moves.append((sr + pm * i,sc + mp * i,0))
                            if board[sr + pm * i][sc + mp * i][0] == "b":
                                self.allowed_moves.append((sr + pm * i,sc + mp * i,1))
                                break
        if board[sr][sc] == "wK":
            for r in [-1,0,1]:
                for c in [-1,0,1]:
                    if sr + r in range(8) and sc + c in range(8) and not r == c == 0:
                        if board[sr + r][sc + c] == "--":
                            self.allowed_moves.append((sr + r, sc + c,0))
                        if board[sr + r][sc + c][0] == "b":
                            self.allowed_moves.append((sr + r, sc + c,1))
        if board[sr][sc] == "bp":
            if sr == 1 and board[sr + 1][sc] == "--" and board[sr-2][sc] == "--":
                for i in [1,2]:
                    self.allowed_moves.append((sr + i,sc,0))
            elif sr + 1 < 8 and board[sr + 1][sc] == "--":
                self.allowed_moves.append((sr + 1,sc,0))
            for i in [-1,1]:
                if sc + i in range(8) and board[sr - 1][sc + i][0] == "w":
                    self.allowed_moves.append((sr + 1,sc + i,1))
        if board[sr][sc] == "bR":
            for pm in [-1,1]:
                for i in range(1,8):
                    if sr + pm * i in range(8):
                        if board[sr + pm * i][sc] == "--":
                            self.allowed_moves.append((sr + pm * i,sc,0))
                        if board[sr + pm * i][sc][0] == "w":
                            self.allowed_moves.append((sr + pm * i,sc,1))
                            break
                for i in range(1,8):
                    if sc + pm * i in range(8):
                        if board[sr][sc + pm * i] == "--":
                            self.allowed_moves.append((sr,sc + pm * i,0))
                        if board[sr][sc + pm * i] == "w":
                            self.allowed_moves.append((sr,sc + pm * i,1))
                            break
        if board[sr][sc] == "bB":
            for pm in [-1,1]:
                for mp in [-1,1]:
                    for i in range(8):
                        if sr + pm * i in range(8) and sc + mp * i in range(8):
                            if board[sr + pm * i][sc + mp * i] == "--":
                                self.allowed_moves.append((sr + pm * i,sc + mp * i,0))
                            if board[sr + pm * i][sc + mp * i][0] == "w":
                                self.allowed_moves.append((sr + pm * i,sc + mp * i,1))
                                break
        if board[sr][sc] == "bN":
            for m in [[1,2],[2,1]]:
                for pm in [-1,1]:
                    for mp in [-1,1]:
                        if sr + m[0] * pm in range(8) and sc + m[1] * mp in range(8):
                            if board[sr + m[0] * pm][sc + m[1] * mp] == "--":
                                self.allowed_moves.append((sr + m[0] * pm,sc + m[1] * mp,0))
                            if board[sr + m[0] * pm][sc + m[1] * mp][0] == "w":
                                self.allowed_moves.append((sr + m[0] * pm,sc + m[1] * mp,1))
        if board[sr][sc] == "bQ":
            for pm in [-1,1]:
                for i in range(1,8):
                    if sr + pm * i in range(8):
                        if board[sr + pm * i][sc] == "--":
                            self.allowed_moves.append((sr + pm * i,sc,0))
                        if board[sr + pm * i][sc][0] == "w":
                            self.allowed_moves.append((sr + pm * i,sc,1))
                            break
                for i in range(1,8):
                    if sc + pm * i in range(8):
                        if board[sr][sc + pm * i] == "--":
                            self.allowed_moves.append((sr,sc + pm * i,0))
                        if board[sr][sc + pm * i] == "w":
                            self.allowed_moves.append((sr,sc + pm * i,1))
                            break
            for pm in [-1,1]:
                for mp in [-1,1]:
                    for i in range(8):
                        if sr + pm * i in range(8) and sc + mp * i in range(8):
                            if board[sr + pm * i][sc + mp * i] == "--":
                                self.allowed_moves.append((sr + pm * i,sc + mp * i,0))
                            if board[sr + pm * i][sc + mp * i][0] == "w":
                                self.allowed_moves.append((sr + pm * i,sc + mp * i,1))
                                break
        if board[sr][sc] == "wK":
            for r in [-1,0,1]:
                for c in [-1,0,1]:
                    if sr + r in range(8) and sc + c in range(8) and not r == c == 0:
                        if board[sr + r][sc + c] == "--":
                            self.allowed_moves.append((sr + r, sc + c,0))
                        if board[sr + r][sc + c][0] == "b":
                            self.allowed_moves.append((sr + r, sc + c,1))
        for i in self.allowed_moves:
            if i[2] == 0:
                pygame.draw.circle(screen,[192,192,192],[32 + i[1] * 64 - 10,32 + i[0] * 64],10,10)
            if i[2] == 1:
                pygame.draw.circle(screen,[192,192,192],[32 + i[1] * 64 - 10,32 + i[0] * 64],25,2)

    def record_move():
        pass


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
        draw_board.draw_text(screen,font_name,i,int(sidelen/28),int(sidelen/8*(7/8 + a)),int(sidelen * 61/64),color[a%2])
        a += 1
    for i in range(1,9):
        draw_text(screen,font_name,str(9-i),int(sidelen/32),int(sidelen/64),int(4+sidelen/8*(i-1)),color[i%2])
