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
        self.movelog1 = []
        self.movelog2 = []
        self.check = False
        self.checkmate = False

class move:
    def __init__(self):
        self.allowed_moves = []
        self.wb = {0:"w",1:"b"}

    def movable(self,board,sr,sc):
        if board[sr][sc] == "--":
            return 1
        if board[sr][sc][1] == "p":
            for i in range(2):
                if board[sr][sc][0] == self.wb[i]:
                    if sr == 6 - i * 5 and board[5 - i * 3][sc] == "--" and board[4 - i][sc] == "--":
                        self.allowed_moves.append((5 - i * 3,sc))
                        self.allowed_moves.append((4 - i,sc))
                    elif sr - 1 + i * 2 in range(8) and board[sr - 1 + i * 2][sc] == "--":
                        self.allowed_moves.append((sr - 1 + i * 2,sc))
                    for j in [-1,1]:
                        if sc + j in range(8) and board[sr - 1 + i * 2][sc + j] == self.wb[i + 1 % 2]:
                            self.allowed_moves.append(sr - 1 + i * 2,sc + j)
                    #if sr == i * 7: #promotion

        if board[sr][sc][1] == "R":
            for i in range(2):
                if board[sr][sc][0] == self.wb[i]:
                    for pm in [-1,1]:
                        for i in range(1,8):
                            if sr + pm * i in range(8):
                                if board[sr + pm * i][sc] == "--":
                                    self.allowed_moves.append((sr + pm * i,sc))
                                if board[sr + pm * i][sc][0] == self.wb[i]:
                                    break
                                if board[sr + pm * i][sc][0] == self.wb[i+1%2]:
                                    self.allowed_moves.append((sr + pm * i,sc))
                                    break
                        for i in range(1,8):
                            if sc + pm * i in range(8):
                                if board[sr][sc + pm * i] == "--":
                                    self.allowed_moves.append((sr,sc + pm * i))
                                if board[sr][sc + pm * i][0] == self.wb[i]:
                                    break
                                if board[sr][sc + pm * i] == self.wb[i+1%2]:
                                    self.allowed_moves.append((sr,sc + pm * i))
                                    break

        if board[sr][sc][1] == "B":
            for i in range(2):
                if board[sr][sc][0] == self.wb[i]:
                    for pm in [-1,1]:
                        for mp in [-1,1]:
                            for i in range(1,8):
                                if sr + pm * i in range(8) and sc + mp * i in range(8):
                                    if board[sr + pm * i][sc + mp * i] == "--":
                                        self.allowed_moves.append((sr + pm * i,sc + mp * i))
                                    if board[sr + pm * i][sc + mp * i][0] == self.wb[i]:
                                        break  
                                    if board[sr + pm * i][sc + mp * i][0] == self.wb[i+1%2]:
                                        self.allowed_moves.append((sr + pm * i,sc + mp * i))
                                        break
        if board[sr][sc][1] == "N":
            for i in range(2):
                if board[sr][sc][0] == self.wb[i]:
                    for m in [[1,2],[2,1]]:
                        for pm in [-1,1]:
                            for mp in [-1,1]:
                                if sr + m[0] * pm in range(8) and sc + m[1] * mp in range(8):
                                    if board[sr + m[0] * pm][sc + m[1] * mp] == "--":
                                        self.allowed_moves.append((sr + m[0] * pm,sc + m[1] * mp))
                                    if board[sr + m[0] * pm][sc + m[1] * mp][0] == self.wb[i+1%2]:
                                        self.allowed_moves.append((sr + m[0] * pm,sc + m[1] * mp))
        if board[sr][sc][1] == "Q":
            for i in range(2):
                if board[sr][sc][0] == self.wb[i]:
                    for pm in [-1,1]:
                        for i in range(1,8):
                            if sr + pm * i in range(8):
                                if board[sr + pm * i][sc] == "--":
                                    self.allowed_moves.append((sr + pm * i,sc))
                                if board[sr + pm * i][sc][0] == self.wb[i]:
                                    break
                                if board[sr + pm * i][sc][0] == self.wb[i+1%2]:
                                    self.allowed_moves.append((sr + pm * i,sc))
                                    break
                        for i in range(1,8):
                            if sc + pm * i in range(8):
                                if board[sr][sc + pm * i] == "--":
                                    self.allowed_moves.append((sr,sc + pm * i))
                                if board[sr][sc + pm * i][0] == self.wb[i]:
                                    break
                                if board[sr][sc + pm * i][0] == self.wb[i+1%2]:
                                    self.allowed_moves.append((sr,sc + pm * i))
                                    break
                    for pm in [-1,1]:
                        for mp in [-1,1]:
                            for i in range(1,8):
                                if sr + pm * i in range(8) and sc + mp * i in range(8):
                                    if board[sr + pm * i][sc + mp * i] == "--":
                                        self.allowed_moves.append((sr + pm * i,sc + mp * i))
                                    if board[sr + pm * i][sc + mp * i][0] == self.wb[i]:
                                        break  
                                    if board[sr + pm * i][sc + mp * i][0] == self.wb[i+1%2]:
                                        self.allowed_moves.append((sr + pm * i,sc + mp * i))
                                        break
        if board[sr][sc][1] == "K":
            for i in range(2):
                if board[sr][sc][0] == self.wb[i]:
                    for r in [-1,0,1]:
                        for c in [-1,0,1]:
                            if sr + r in range(8) and sc + c in range(8) and not r == c == 0:
                                if board[sr + r][sc + c] == "--":
                                    self.allowed_moves.append((sr + r, sc + c))
                                if board[sr + r][sc + c][0] == self.wb[i+1%2]:
                                    self.allowed_moves.append((sr + r, sc + c))

    def display_move(self,screen,board):
        for i in self.allowed_moves:
            if board[i[0]][i[1]] == "--":
                pygame.draw.circle(screen,[192,192,192],[32 + i[1] * 64,32 + i[0] * 64],10,10)
            else:
                pygame.draw.circle(screen,[192,192,192],[32 + i[1] * 64,32 + i[0] * 64],30,2)

    def record_move(log,sr,sc,er,ec):
        rowdic = {0:"8",1:"7",2:"6",3:"5",4:"4",5:"3",6:"2",7:"1"}
        coldic = {0:"a",1:"b",2:"c",3:"d",4:"e",5:"f",6:"g",7:"h"}
        move = rowdic[sr]+coldic[sc]+rowdic[er]+coldic[ec]
        log.append(move)

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
