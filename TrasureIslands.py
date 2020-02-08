def numberIslands(rows, column, grid):
    visited = [[0 for i in range(rows)] for j in range(column)]


    count = 0
    for i in range(rows):
        for j in range(column):
            if grid[i][j] == 1 and visited[i][j] != 1:
                visited[i][j] = 1
                visitAdjecentsExceptDiagonal(rows, column, grid, visited, i, j)
                count = count + 1
    return count

def visitAdjecentsExceptDiagonal(rows, column, grid, visited, targetRow, targetCol):
    j = targetCol
    for i in range(targetRow+1, rows):
        if(verifyAndMove(rows, column, grid, visited, i, j) == False):
            break    

    for i in range(targetRow-1, 0):
        if(verifyAndMove(rows, column, grid, visited, i, j) == False):
            break
   
    i = targetRow
    for j in range(targetCol+1, column):
        if(verifyAndMove(rows, column, grid, visited, i, j) == False):
            break
   
    for j in range(targetCol-1, 0):
        if(verifyAndMove(rows, column, grid, visited, i, j) == False):
            break