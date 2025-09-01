# Description
# There is an m x n grid where you are allowed to move either down or to the right at any point in time.
#
# Given the two integers m and n, return the number of possible unique paths that can be taken from the top-left corner of the grid (grid[0][0]) to the bottom-right corner (grid[m - 1][n - 1]).
#
# You may assume the output will fit in a 32-bit integer.

class UniquePaths:
    def uniquePaths(self,m:int,n:int):

        memo = [[-1] *  n for _  in range(m)]

        def dfs(i,j):

            if i == m-1 and j == n-1:
                return 1

            if i >= m or j >= n:
                return 0

            if memo[i,j]:
                return memo[i][j]

            memo[i][j] = dfs(i+1,j) + dfs(i,j+1)
            return memo[i][j]


        return dfs(0,0)