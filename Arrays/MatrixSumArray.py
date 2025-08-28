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
