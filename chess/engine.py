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
        self.special_moves = [[],[],[]] #Castling,En passant,Promotion
        self.color = {0:"w",1:"b"}
        self.castling = [[True,True],[True,True]]
        self.rowdic = {0:"8",1:"7",2:"6",3:"5",4:"4",5:"3",6:"2",7:"1"}
        self.coldic = {0:"a",1:"b",2:"c",3:"d",4:"e",5:"f",6:"g",7:"h"}

    def sellect_allowed_moves(self,board,movelog,sr,sc):
        if board[sr][sc] == "--":
            return 1
        if board[sr][sc][1] == "p":
            for color in range(2):
                if board[sr][sc][0] == self.color[color]:
                    if sr == 6 - color * 5 and board[5 - color * 3][sc] == "--" and board[4 - color][sc] == "--":
                        self.allowed_moves.append((5 - color * 3,sc))
                        self.allowed_moves.append((4 - color,sc))
                    elif sr - 1 + color * 2 in range(8) and board[sr - 1 + color * 2][sc] == "--":
                        self.allowed_moves.append((sr - 1 + color * 2,sc))
                        if sr == 1 + color * 5:
                            self.special_moves[2].append((sr - 1 + color * 2,sc))
                    for i in [-1,1]:
                        if sc + i in range(8) and (board[sr - 1 + color * 2][sc + i][0] == self.color[(color + 1) % 2]):
                            self.allowed_moves.append((sr - 1 + color * 2,sc + i))
                        if sc + i in range(8) and (sr - 2 + color * 4 in range(8)) and (
                            board[sr][sc + i][0] == self.color[(color + 1)% 2]) and (movelog[len(movelog) - 1] ==
                            str(self.coldic[sc + i] + self.rowdic[sr - 2 + color * 4] + self.coldic[sc + i] + self.rowdic[sr])
                            ) and (board[sr - 1 + color * 2][sc + i] == "--") and (sr == 3 + color):
                            self.special_moves[1].append((sr - 1 + color * 2,sc + i))
                            self.allowed_moves.append((sr - 1 + color * 2,sc + i))
                        if sr == 1 + color * 5:
                            self.special_moves[2].append((sr - 1 + color * 2,sc + i))

        if board[sr][sc][1] == "R":
            for color in range(2):
                if board[sr][sc][0] == self.color[color]:
                    for rc in [[0,1],[0,-1],[1,0],[-1,0]]:
                        for i in range(1,8):
                            r = sr + rc[0] * i
                            c = sc + rc[1] * i
                            if r in range(8) and c in range(8):
                                if board[r][c] == "--":
                                    self.allowed_moves.append((r,c))
                                if board[r][c][0] == self.color[color]:
                                    break
                                if board[r][c][0] == self.color[(color+1)%2]:
                                    self.allowed_moves.append((r,c))
                                    break

        if board[sr][sc][1] == "B":
            for color in range(2):
                if board[sr][sc][0] == self.color[color]:
                    for rc in [[1,1],[-1,1],[1,-1],[-1,-1]]:
                        for i in range(1,8):
                            r = sr + rc[0] * i
                            c = sc + rc[1] * i
                            if r in range(8) and c in range(8):
                                if board[r][c] == "--":
                                    self.allowed_moves.append((r,c))
                                if board[r][c][0] == self.color[color]:
                                    break  
                                if board[r][c][0] == self.color[(color+1)%2]:
                                    self.allowed_moves.append((r,c))
                                    break
        if board[sr][sc][1] == "N":
            for color in range(2):
                if board[sr][sc][0] == self.color[color]:
                    for rc in [[1,2],[2,1],[-1,2],[-2,1],[1,-2],[2,-1],[-1,-2],[-2,-1]]:
                        r = sr + rc[0]
                        c = sc + rc[1]
                        if r in range(8) and c in range(8):
                            if board[r][c] == "--":
                                self.allowed_moves.append((r,c))
                            if board[r][c][0] == self.color[(color+1)%2]:
                                self.allowed_moves.append((r,c))
        if board[sr][sc][1] == "Q":
            for color in range(2):
                if board[sr][sc][0] == self.color[color]:
                    for rc in [[0,1],[0,-1],[1,0],[-1,0],[1,1],[-1,1],[1,-1],[-1,-1]]:
                        for i in range(1,8):
                            r = sr + rc[0] * i
                            c = sc + rc[1] * i
                            if r in range(8) and c in range(8):
                                if board[r][c] == "--":
                                    self.allowed_moves.append((r,c))
                                if board[r][c][0] == self.color[color]:
                                    break
                                if board[r][c][0] == self.color[(color+1)%2]:
                                    self.allowed_moves.append((r,c))
                                    break
        if board[sr][sc][1] == "K":
            for color in range(2):
                if board[sr][sc][0] == self.color[color]:
                    for r in [-1,0,1]:
                        for c in [-1,0,1]:
                            if sr + r in range(8) and sc + c in range(8) and not r == c == 0:
                                if board[sr + r][sc + c] == "--":
                                    self.allowed_moves.append((sr + r, sc + c))
                                if board[sr + r][sc + c][0] == self.color[(color+1)%2]:
                                    self.allowed_moves.append((sr + r, sc + c))
                    for ks in movelog:
                        if ks[0:2] == ("e" + str(1+7*color)):
                            self.castling[color] = [False,False]
                        if ks[0:2] == ("h" + str(1+7*color)):
                            self.castling[color][0] = [False]
                        if ks[0:2] == ("a" + str(1+7*color)):
                            self.castling[color][1] = [False]
                    r = 7 - color * 7
                    if (self.castling[color][0]) and (not self.isthreated(board,r,4)) and (
                        not self.isthreated(board,r,5)) and (not self.isthreated(board,r,6)
                        ) and (board[r][5] == board[r][6] == "--"):
                        self.special_moves[0].append((r,6))
                        self.allowed_moves.append((r,6))
                    if (self.castling[color][0]) and (not self.isthreated(board,r,4)) and (
                        not self.isthreated(board,r,3)) and (not self.isthreated(board,r,2)
                        )and (not self.isthreated(board,r,1)) and (
                        board[r][3] == board[r][2] == board[r][1] == "--"):
                        self.special_moves[0].append((r,2))
                        self.allowed_moves.append((r,2))

    def isthreated(self,board,r,c):
        return False

    def check():
        pass

    def move_piece(self,board,sr,sc,er,ec):
        if (er,ec) in self.special_moves[0]:
            board[er][ec] = board[sr][sc]
            board[sr][sc] = "--"
            if ec == 6:
                board[er][5] = board[er][7]
                board[er][7] = "--"
            if ec == 2:
                board[er][3] = board[er][0]
                board[er][0] = "--"
        elif (er,ec) in self.special_moves[1]:
            board[er][ec] = board[sr][sc]
            board[sr][sc] = "--"
            if er == 2:
                board[3][ec] = "--"
            if er == 5:
                board[4][ec] = "--"
        elif (er,ec) in self.special_moves[2]:
            print("promotion")
        else:
            board[er][ec] = board[sr][sc]
            board[sr][sc] = "--"

    def display_allowed_move(self,screen,board):
        for i in self.allowed_moves:
            if i in self.special_moves[0]:
                pygame.draw.circle(screen,[135,206,250],[32 + i[1] * 64,32 + i[0] * 64],10,10)
            elif board[i[0]][i[1]] == "--":
                pygame.draw.circle(screen,[192,192,192],[32 + i[1] * 64,32 + i[0] * 64],10,10)
            else:
                pygame.draw.circle(screen,[192,192,192],[32 + i[1] * 64,32 + i[0] * 64],30,2)

    def record_move(self,movelog,sr,sc,er,ec):
        move = self.coldic[sc]+self.rowdic[sr]+self.coldic[ec]+self.rowdic[er]
        movelog.append(move)

def draw_text(screen,font_name,text,size,x,y,color):
    font = pygame.font.Font(font_name,size)
    text_surface = font.render(text,True,color)
    text_rect = text_surface.get_rect()
    text_rect.centerx = x
    text_rect.top = y
    screen.blit(text_surface,text_rect)

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
