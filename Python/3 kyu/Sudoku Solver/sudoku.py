global flag, row, col, block


def sudoku(board):
    
    global flag, row, col, block
    
    def dfs(board, index):
        global flag, row, col, block
        if flag == 1:
            return
        if index > 80:
            flag = 1
            return
        i, j = index / 9, index % 9
        if board[i][j] != 0:
            return dfs(board, index + 1)
        for k in xrange(9):
            if row[i][k] or col[j][k] or block[i / 3 * 3 + j / 3][k]:
                continue
            board[i][j] = k + 1
            row[i][k], col[j][k] = True, True
            block[i / 3 * 3 + j / 3][k] = True
            dfs(board, index + 1)
            if flag == 1:
                return
            block[i / 3 * 3 + j / 3][k] = False
            col[j][k], row[i][k] = False, False
            board[i][j] = 0
    
    flag = 0
    row = [[False for j in xrange(9)] for i in xrange(9)]
    col = [[False for j in xrange(9)] for i in xrange(9)]
    block = [[False for j in xrange(9)] for i in xrange(9)]
    for i in xrange(9):
        for j in xrange(9):
            if not board[i][j]:
                continue
            row[i][board[i][j] - 1] = True
            col[j][board[i][j] - 1] = True
            block[i / 3 * 3 + j / 3][board[i][j] - 1] = True
    dfs(board, 0)
    if flag:
        return board
    else:
        return []


if __name__ == '__main__':
    print(sudoku([
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]))
