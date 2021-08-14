import random 
import numpy as np


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
        
        


B=create_board()
print(B)
placeeach(B)
