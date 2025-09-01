# Description
# Given an array nums of unique integers, return all possible subsets of nums.
#
# The solution set must not contain duplicate subsets. You may return the solution in any order.
#
# Example 1:
#
# Input: nums = [1,2,3]
#
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

from typing import List

class UniqueSubsets:
    def uniqueSubests(self,nums: List[int]):

        res = []
        subSet = []

        def dfs(i):

            if i >= len(nums):
                res.append(subSet.copy())
                return
            subSet.append(nums[i])
            dfs(i+1)
            subSet.pop()
            dfs(i+1)
        dfs(0)
        return res
