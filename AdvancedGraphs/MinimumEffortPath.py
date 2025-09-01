# Description
# You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.
#
# A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.
#
# Return the minimum effort required to travel from the top-left cell to the bottom-right cell.
#
# Example 1:
#
# Input: heights = [
#     [1,1,1],
#     [3,2,4],
#     [2,5,4]
# ]
#
# Output: 2

from typing import List
import heapq
class MinimumEffortPath:

    def minimumEffortPath(self,heights: List[List[int]]):

        Rows = len(heights)
        Cols = len(heights[0])

        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        minHeap = [[0,0,0]] #Difference, Row,Col
        visited = set()

        while minHeap:
            diff ,row,col = minHeap.pop()

            if (row,col) in visited:
                continue

            if row == Rows-1 and col == Cols -1:
                return diff

            visited.add((row,col))

            for nr,nc in directions:
                newRow = row + nr
                newCol = col + nc
                if (newRow < 0 or newRow >= Rows or col < 0 or col >= Cols or
                        (newRow,newCol) in visited):
                    continue

                newDiff = max(diff,abs(heights[row][col] - heights[newRow][newCol]))
                heapq.heappush(minHeap,[newDiff,newRow,newCol])





