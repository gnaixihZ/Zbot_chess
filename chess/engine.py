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
        self.check = [False,False]
        self.checkmate = False

class move:
    def __init__(self):
        self.allowed_moves = []
        self.threated_squares = [[],[]]
        self.special_moves = [[],[],[]] #Castling,En passant,Promotion
        self.color = {0:"w",1:"b"}
        self.castling = [[True,True],[True,True]]
        self.rowdic = {0:"8",1:"7",2:"6",3:"5",4:"4",5:"3",6:"2",7:"1"}
        self.coldic = {0:"a",1:"b",2:"c",3:"d",4:"e",5:"f",6:"g",7:"h"}
        self.wk = (7,4)
        self.bk = (0,4)

    def find_allowed_moves(self,board,movelog,sr,sc):
        if board[sr][sc] == "--":
            return 1
        elif board[sr][sc][0] == "w":
            color = 0
        else:
            color = 1
        if board[sr][sc][1] == "p":
            self.pawn_move(board,movelog,sr,sc,color)
        if board[sr][sc][1] == "R":
            self.rook_move(board,sr,sc,color)
        if board[sr][sc][1] == "B":
            self.bishop_move(board,sr,sc,color)
        if board[sr][sc][1] == "N":
            self.knight_move(board,sr,sc,color)
        if board[sr][sc][1] == "Q":
            self.queen_move(board,sr,sc,color)
        if board[sr][sc][1] == "K":
            self.king_move(board,movelog,sr,sc,color)

        # for i in self.allowed_moves:
        #     if not self.test_check(board,sr,sc,i[0],i[1]):
        #         self.allowed_moves.remove(i)
        #         print(self.allowed_moves)

    def pawn_move(self,board,movelog,sr,sc,color):
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
    
    def rook_move(self,board,sr,sc,color):
        for rc in [[0,1],[0,-1],[1,0],[-1,0]]:
            for i in range(1,8):
                r = sr + rc[0] * i
                c = sc + rc[1] * i
                if r in range(8) and c in range(8):
                    if board[r][c] == "--":
                        self.allowed_moves.append((r,c))
                    if board[r][c][0] == self.color[color]:
                        break
                    if board[r][c][0] == self.color[(color + 1) % 2]:
                        self.allowed_moves.append((r,c))
                        break

    def bishop_move(self,board,sr,sc,color):
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

    def knight_move(self,board,sr,sc,color):
        for rc in [[1,2],[2,1],[-1,2],[-2,1],[1,-2],[2,-1],[-1,-2],[-2,-1]]:
            r = sr + rc[0]
            c = sc + rc[1]
            if (r in range(8) and c in range(8)) and (board[r][c] == "--" or 
            board[r][c][0] == self.color[(color+1)%2]):
                self.allowed_moves.append((r,c))
    
    def queen_move(self,board,sr,sc,color):
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
    
    def king_move(self,board,movelog,sr,sc,color):
        for r in [-1,0,1]:
            for c in [-1,0,1]:
                if sr + r in range(8) and sc + c in range(8) and not r == c == 0:
                    if board[sr + r][sc + c] == "--" or board[sr + r][sc + c][0] == self.color[(color+1)%2]:
                        self.allowed_moves.append((sr + r, sc + c))
        for ks in movelog:
            if ks[0:2] == ("e" + str(1+7*color)):
                self.castling[color] = [False,False]

            if ks[0:2] == ("h" + str(1+7*color)):
                self.castling[color][0] = [False]

            if ks[0:2] == ("a" + str(1+7*color)):
                self.castling[color][1] = [False]
        r = 7 - color * 7
        if (self.castling[color][0],self.isthreated(board,r,4),self.isthreated(board,r,5),self.isthreated(board,r,6)
            ) == (True,False,False,False) and (board[r][5] == board[r][6] == "--"):
            self.special_moves[0].append((r,6))
            self.allowed_moves.append((r,6))
        if (self.castling[color][0],self.isthreated(board,r,4),self.isthreated(board,r,3),
            self.isthreated(board,r,2),self.isthreated(board,r,1)) == (True,False,False,False,False
            ) and (board[r][3] == board[r][2] == board[r][1] == "--"):
            self.special_moves[0].append((r,2))
            self.allowed_moves.append((r,2))
        
    def find_threated_square(self,board):
        a = self.allowed_moves
        for r in range(8):
            for c in range(8):
                self.allowed_moves = []
                if board[r][c][0] == "w":
                    color = 0
                elif board[r][c][0] == "b":
                    color = 1
                if board[r][c][1] == "p":
                    for i in [-1,1]:
                        if c + i in range(8) and (board[r - 1 + color * 2][c + i][0] == self.color[(color + 1) % 2] or 
                        board[r - 1 + color * 2][c + i] == "--"):
                            if (r - 1 + color * 2,c + i) not in self.threated_squares[color]:
                                self.threated_squares[color].append((r - 1 + color * 2,c + i))
                if board[r][c][1] == "R":
                    self.rook_move(board,r,c,color)
                    for i in self.allowed_moves:
                        if i not in self.threated_squares[color]:
                            self.threated_squares[color].append(i)
                if board[r][c][1] == "B":
                    self.bishop_move(board,r,c,color)
                    for i in self.allowed_moves:
                        if i not in self.threated_squares[color]:
                            self.threated_squares[color].append(i)
                if board[r][c][1] == "N":
                    self.knight_move(board,r,c,color)
                    for i in self.allowed_moves:
                        if i not in self.threated_squares[color]:
                            self.threated_squares[color].append(i)
                if board[r][c][1] == "Q":
                    self.queen_move(board,r,c,color)
                    for i in self.allowed_moves:
                        if i not in self.threated_squares[color]:
                            self.threated_squares[color].append(i)
                if board[r][c][1] == "K":
                    for i in [-1,0,1]:
                        for j in [-1,0,1]:
                            if r + i in range(8) and c + j in range(8) and not i == j == 0:
                                if board[r + i][c + j] == "--" or board[r + i][c + j][0] == self.color[(color+1)%2]:
                                    if (r + i, c + j) not in self.threated_squares[color]:
                                        self.threated_squares[color].append((r + i, c + j))
        self.allowed_moves = a

    def isthreated(self,board,r,c):
        self.find_threated_square(board)
        if board[r][c][0] == "w":
            color = 0
        elif board[r][c][0] == "b":
            color = 1
        else:
            if r == 0:
                color = 1
            if r == 7:
                color = 0
        if (r,c) in self.threated_squares[(color + 1) % 2]:
            return True
        return False

    def ischecked(self,board,color):
        if color == 0:
            if self.isthreated(board,self.wk[0],self.wk[1]):
                return True
            else:
                return False
        else:
            if self.isthreated(board,self.bk[0],self.bk[1]):
                return True
            else:
                return False
    
    def test_check(self,board,sr,sc,er,ec):
        if board[sr][sc][0] == "w":
            color = 0
        elif board[sr][sc][0] == "b":
            color = 1
        else:
            return 1
        testboard = board
        for i in testboard:
            print(i)
        testboard[er][ec] = testboard[sr][sc]
        testboard[sr][sc] = "--"
        if self.ischecked(testboard,color):
            return False
        else:
            return True

    def move_piece(self,board,sr,sc,er,ec):
        if (er,ec) in self.special_moves[0]:
            board[er][ec] = board[sr][sc]
            board[sr][sc] = "--"
            if board[er][ec] == "wK":
                self.wk = (er,ec)
            else:
                self.bk = (er,ec)
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
            board[er][ec] = board[sr][sc][0] + "Q"
            board[sr][sc] = "--"
            # self.display_promotion()
        else:
            if board[sr][sc] == "wK":
                self.wk = (er,ec)
            if board[sr][sc] == "bK":
                self.bk = (er,ec)
            board[er][ec] = board[sr][sc]
            board[sr][sc] = "--"

    def display_promotion():
        pass

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
