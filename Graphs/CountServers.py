# Description
# You are given a map of a server center, represented as a m * n integer matrix grid, where 1 means that on that cell there is a server and 0 means that it is no server. Two servers are said to communicate if they are on the same row or on the same column.
#
# Return the number of servers that communicate with any other server.
#
# Example 1:
#
# Input: grid = [
#     [1,1,0,0],
#     [0,0,1,0],
#     [0,0,1,0],
#     [0,0,0,1]
# ]
#
# Output: 4

from typing import List

class CountServers:
    def countServers(self,grid : List[List[int]]):

        Rows = [0] * len(grid)
        Cols = [0] * len(grid[0])

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    Rows[row] += 1
                    Cols[col] += 1

        res = 0
        for r in range(Rows) :
            for c in range(Cols):
                if grid[r][c] == 1 and max(Rows[r],Cols[c]) > 1:
                    res += 1

        return res


