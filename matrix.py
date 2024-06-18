mat = [[1,2,3],[4,5,6],[7,8,9]]
'''
1 2 3
4  5 6
7 8 9
'''

def print_matrix(mat):
    mat_len = len(mat)

    for i in range(mat_len):
        for j in range(i,mat_len):
            print("d")
        print(mat[i],mat[j])


#print_matrix(mat)

from typing import List
def hIndex( citations: List[int]) -> int:
    citations.sort()
    if citations and len(citations) > 2:

        c_len = len(citations) // 2
        return citations[c_len]
    else:
        print(citations)
        return  citations[-1]

print(hIndex([0,1]))


def diagonalDIfference(mat: List[List[int]]) -> int:
    mat_len = len(mat)
    for i in range(mat_len):
        for j in range(mat_len):
            if i == j:
                print(mat[i][j])
