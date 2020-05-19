  
#766. Toeplitz Matrix
#Author: Ana Luisa Mata

#A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.
#Now given an M x N matrix, return True if and only if the matrix is Toeplitz.

#Runtime: 96 ms, faster than 24.30% of Python3 online submissions for Toeplitz Matrix.
#Memory Usage: 13.9 MB, less than 7.14% of Python3 online submissions for Toeplitz Matrix.
#Time complexity: O(n^2)
#Space complexity: O(1)

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        
        for col in range(cols-1):
            for row in range(rows-1):
                if matrix[row][col] != matrix[row+1][col+1]:
                    return False
        return True
