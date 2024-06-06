from typing import List

def spiralOrder(matrix: List[List[int]]):
    top , left = 0, 0
    bottom, right = len(matrix) - 1, len(matrix[0]) - 1
    ans = []

    while left<= right and top<=bottom:
        for i in range(left, right+1):
            ans.append(matrix[top][i])
        top += 1

        for i in range(top, bottom+1):
            ans.append(matrix[i][right])
        right -=1

        if top<=bottom:
            for i in range(right, left-1, -1):
                ans.append(matrix[bottom][i])
            bottom -= 1

        if left<=right:
            for i in range(bottom,top-1,-1):
                ans.append(matrix[i][left])
            left=left+1
    return ans


data = [[1,2,3],[4,5,6],[7,8,9]]
ans= spiralOrder(data)
print(ans)
     