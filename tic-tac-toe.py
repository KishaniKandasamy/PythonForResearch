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
    if np.any(np.all(board==player, axis=1)): # this checks if any row contains all positions equal to player-------------> OR if(np.any([np.all(board[i] == player) for i in range(board.shape[0])])):
        return True
    else:
        return False
    
     
def col_win(board, player):
     if np.any(np.all(board==player, axis=0)): # this checks if any column  contains all positions equal to player.
        return True
     else:
        return False

def diag_win(board, player):
    if np.all(np.diag(board)==player) or np.all(np.diag(np.fliplr(board))==player):
        # np.diag returns the diagonal of the array
        # np.fliplr rearranges columns in reverse order
        return True
    else:
        return False
    
def evaluate(board):
    winner = 0
    for player in [1, 2]:
        if row_win(board, player) or col_win(board, player) or diag_win(board, player):
            winner = player
        pass
    if np.all(board != 0) and winner == 0:
        winner = -1
    return winner
    
  
    

B=create_board()
print(B)
placeeach(B)
print(B)
evaluate(B)


