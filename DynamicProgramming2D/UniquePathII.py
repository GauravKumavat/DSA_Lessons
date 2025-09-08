# You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.
#
# An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.
#
# Return the number of possible unique paths that the robot can take to reach the bottom-right corner.
#
# The testcases are generated so that the answer will be less than or equal to 2 * 109.

from typing import List

class UniquePathII:
    def uniquePath(self,grid : List[List[int]]):
        M,N = len(grid),len(grid[0])
        dp = [0] * N
        dp[N-1] = 1

        for row in reversed(range(M)):
            for col in reversed(range(N)):
                if grid[row][col]:
                    dp[col] = 0
                if col + 1 < N:
                    dp[col] = dp[col] + dp[col+1]
        return dp[0]
