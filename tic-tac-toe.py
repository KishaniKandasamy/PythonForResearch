import random 
import numpy as np
#random.seed(1)

def create_board():
    board= np.zeros((3,3), dtype=int)
    return board

def place(board, player, position):
    board[position[0],position[1]]=player
    return board
     
def possibilities(board):
    solutions = np.argwhere(board == 0)
    aposibility = random.choice(solutions)
    return aposibility
    
def random_place(board, player):
        ind=possibilities(board)
        updatedboard=place(board,player,ind)
        return updatedboard
    
def placeeach(board):
    for i in range(9):
        if(i%2==0):
            board=random_place(board,1)
        else:
            board=random_place(board,2)
    return board
        
def row_win(board, player):
    if(np.any([np.all(board[i] == player) for i in range(board.shape[0])])):
        return True
    else:
        return False
  
    

B=create_board()
print(B)
placeeach(B)
print(B)
row_win(B,2)

