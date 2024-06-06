from typing import List
def rotate_image(matrix : List[List[int]]) -> List[List[int]]:
    n = len(matrix)
    # transpose matrix
    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    #reverse each row
    for i in range(n):
        matrix[i].reverse()