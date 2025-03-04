import numpy as np
import pygame , sys 
ROW_COUNT = 6
COLUMN_COUNT = 7

def create_board():
    borad = np.zeros((ROW_COUNT,COLUMN_COUNT) , dtype='int')
    return borad

def drop(board , col , row , piece):
    board[row][col] = piece
    
def isvalid_location(board ,col):
    return board[0][col] == 0

def get_next_open_row(board, col):
    for r in range(ROW_COUNT-1 , -1 , -1):
        if board[r][col] == 0 :
            return r

def win_or_not(board , piece):
    global game_over , label
    def getMaxLength(arr , n):
        count = 0
        result = 0

        for i in range(len(arr)):
            
            if (arr[i] != n):
                count = 0
            else:
                count+= 1
                result = max(result, count)
        return result
    for i in board:
        if getMaxLength(i.tolist() , piece) == 4:
            label = myfont.render("Player 1 wins" if piece == 1 else "Player 2 wins" ,False, 'pink')
            game_over = True
    else :
        for i in np.transpose(board):
            if getMaxLength(i.tolist() , piece) == 4:
                label = myfont.render("Player 1 wins" if piece == 1 else "Player 2 wins" , 1 , 'pink')
                game_over = True
        else:
            for i in range(3) :
                for j in range(4) :
                    if np.array_equal(np.diag(board[i:i+4,j:j+4]),np.diag(np.full((4,4),piece))) or np.array_equal(np.diag(np.flip(board[i:i+4,j:j+4],axis=0)),np.diag(np.full((4,4),piece))):
                        label = myfont.render("Player 1 wins" if piece == 1 else "Player 2 wins" , 1 , "pink")
                        game_over = True
     
def draw_board(board) :
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen,"white", (c*sqr_size,r*sqr_size + sqr_size,sqr_size,sqr_size) )
            if board[r][c] == 0 :
                pygame.draw.circle(screen , "black" , (c*sqr_size + sqr_size//2,r*sqr_size + sqr_size + sqr_size//2),(sqr_size // 2.001))
            elif board[r][c] == 1:
                pygame.draw.circle(screen , "yellow" , (c*sqr_size + sqr_size//2,r*sqr_size + sqr_size + sqr_size//2),(sqr_size // 2.001))
            else : 
                pygame.draw.circle(screen , "orange" , (c*sqr_size + sqr_size//2,r*sqr_size + sqr_size + sqr_size//2),(sqr_size // 2.001))
    pygame.display.update()

board = create_board()

global game_over
game_over = False

turn = 0

pygame.init()


#Getting the Screen ready :
sqr_size = 100
myfont = pygame.font.SysFont("monospace" , 40 , bold=True)

width = COLUMN_COUNT * sqr_size
height =( ROW_COUNT + 1 ) * sqr_size
size = (width , height)

screen = pygame.display.set_mode(size)

draw_board(board) 
pygame.display.update()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen , "black" , (0, 0 , width , sqr_size))
            posx = event.pos[0]
            if turn == 0 :
                pygame.draw.circle(screen , "yellow" , (posx,sqr_size // 2), sqr_size // 2.001)
            else:
                pygame.draw.circle(screen , "orange" , (posx,sqr_size // 2), sqr_size // 2.001)
            pygame.display.update()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pass
            if turn == 0:
                posx = event.pos[0]
                col = posx // sqr_size       
                if isvalid_location(board,col):
                    row = get_next_open_row(board ,col)
                    drop(board , col, row , 1)
                    draw_board(board)
                    win_or_not(board , 1)
            else:
                posx = event.pos[0]
                col = posx // sqr_size  
                if isvalid_location(board,col):
                    row = get_next_open_row(board ,col)
                    drop(board , col, row , 2)
                    draw_board(board)
                    win_or_not(board , 2)
            turn += 1
            turn %= 2 
            if game_over == True:
                pygame.draw.rect(screen , "red" , (180 , 300 , width // 2, sqr_size-30))
                screen.blit(label,(200,310))
                pygame.display.update()
                pygame.time.wait(3000)
    