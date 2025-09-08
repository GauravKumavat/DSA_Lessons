# You are given an array of integers heights of size n representing a row of buildings, where heights[i] is the height of the ith building.
#
# There is an ocean located to the far right of the buildings. A building has an ocean view if every building to its right is strictly shorter than it.
#
# Return a list of indices (0-indexed) of the buildings that have an ocean view, sorted in increasing order.
#
# Example 1:
#
# Input: heights = [4,2,3,2,1]
#
# Output: [0,2,3,4]

from typing import List


class BuildingWithOceanView:
    def findBuilding(self,heights: List[int]):

        res = [len(heights)-1]

        for i in range(len(heights)-2 , -1,-1) :
            if res[-1] < heights[i]:
                res.append(heights[i])
            else:
                continue

        return res.reverse()
