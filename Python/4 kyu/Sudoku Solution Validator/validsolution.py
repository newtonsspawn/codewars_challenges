import numpy as np


def validSolution(board):
    
    board = np.array(board)
    
    valid_list = list(range(1, 10))
    
    for row in board:
        if 0 in row:
            return False
        if sorted(row) != valid_list:
            return False
    
    for column in board.T:
        if sorted(column) != valid_list:
            return False
    
    for i, j in [(0, 0), (3, 0), (6, 0),
                 (0, 3), (3, 3), (6, 3),
                 (0, 6), (3, 6), (6, 6)]:
        sub = []
        for x_r in range(0, 3):
            for y_r in range(0, 3):
                sub.append(board[i+x_r][j+y_r])
        if sorted(sub) != valid_list:
            return False
    
    return True
    

if __name__ == '__main__':
    print(validSolution(
                [[5, 3, 4, 6, 7, 8, 9, 1, 2],
                 [6, 7, 2, 1, 9, 5, 3, 4, 8],
                 [1, 9, 8, 3, 4, 2, 5, 6, 7],
                 [8, 5, 9, 7, 6, 1, 4, 2, 3],
                 [4, 2, 6, 8, 5, 3, 7, 9, 1],
                 [7, 1, 3, 9, 2, 4, 8, 5, 6],
                 [9, 6, 1, 5, 3, 7, 2, 8, 4],
                 [2, 8, 7, 4, 1, 9, 6, 3, 5],
                 [3, 4, 5, 2, 8, 6, 1, 7, 9]]))
    print(validSolution(
                [[5, 3, 4, 6, 7, 8, 9, 1, 2],
                 [6, 7, 2, 1, 9, 0, 3, 4, 9],
                 [1, 0, 0, 3, 4, 2, 5, 6, 0],
                 [8, 5, 9, 7, 6, 1, 0, 2, 0],
                 [4, 2, 6, 8, 5, 3, 7, 9, 1],
                 [7, 1, 3, 9, 2, 4, 8, 5, 6],
                 [9, 0, 1, 5, 3, 7, 2, 1, 4],
                 [2, 8, 7, 4, 1, 9, 6, 3, 5],
                 [3, 0, 0, 4, 8, 1, 1, 7, 9]]))
    print(validSolution(
                [[1, 3, 2, 5, 7, 9, 4, 6, 8],
                 [4, 9, 8, 2, 6, 1, 3, 7, 5],
                 [7, 5, 6, 3, 8, 4, 2, 1, 9],
                 [6, 4, 3, 1, 5, 8, 7, 9, 2],
                 [5, 2, 1, 7, 9, 3, 8, 4, 6],
                 [9, 8, 7, 4, 2, 6, 5, 3, 1],
                 [2, 1, 4, 9, 3, 5, 6, 8, 7],
                 [3, 6, 5, 8, 1, 7, 9, 2, 4],
                 [8, 7, 9, 6, 4, 2, 1, 5, 3]]))
