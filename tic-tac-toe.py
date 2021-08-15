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

    
def play_game():
    board = create_board()
    winner = 0
    while winner == 0:
        for player in [1, 2]:
            random_place(board, player)
            winner = evaluate(board)
            if winner != 0:
                break
    return winner
    
       
results = []   
for i in range(1000):    
    results.append(play_game())
    

results.count(1)

 
