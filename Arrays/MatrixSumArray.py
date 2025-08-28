# Range Sum Query 2D Immutable
# You are given a 2D matrix matrix, handle multiple queries of the following type:
#
# Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
# Implement the NumMatrix class:
#
# NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
# int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
# You must design an algorithm where sumRegion works on O(1) time complexity.
# Example 1:
#
# Input: ["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
# [[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]
#
# Output: [null, 8, 11, 12]



from typing import List

class MatrixSumArray:
    def __init__(self,matrix : List[List[int]]):

        Rows = len(matrix)
        Cols = len(matrix[0])

        self.sumMatrix = [[0] * (Cols+1) for row in range(Rows+1)]

        for row in range(Rows):
            prefixSum = 0
            for col in range(Cols):
                prefixSum += matrix[row][col]
                above = self.sumMatrix[row][col+1]
                self.sumMatrix[row+1][col+1] = prefixSum + above

    def sumRegion(self,r1,c1,r2,c2):
        r1,c2,r2,c2 = r1+1,c1+1,r2+1,c2+1
        bottomRight = self.sumMatrix[r2][c2]
        left = self.sumMatrix[r2][c1-1]
        above = self.sumMatrix[r1-1][c2]
        top = self.sumMatrix[r1-1][c1-1]

        return bottomRight - left - above + top

obj = MatrixSumArray([[1,2,3],
                      [2,3,4],
                      [3,4,5]

])

print(obj.sumRegion(1,1,2,2))
