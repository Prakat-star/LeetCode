from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for row in matrix:
            row.reverse()

# what we need to do and how the program works:
#  the matrix given
#    [0,0 0,1 0,2
#     1,0 1,1 1,2
#     2,0 2,1 2,2 ]

#  the matrix becomes this after the first 2D loop
#    [1 4 7
#     2 5 8 
#     3 6 9 ]

#  after reversing the rows in the matrix we get after first 2D loop
#   [7 4 1
#    8 5 2
#    9 6 3]