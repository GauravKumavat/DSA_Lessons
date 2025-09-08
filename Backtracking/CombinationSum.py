# You are given an array of distinct integers nums and a target integer target. Your task is to return a list of all unique combinations of nums where the chosen numbers sum to target.
#
# The same number may be chosen from nums an unlimited number of times. Two combinations are the same if the frequency of each of the chosen numbers is the same, otherwise they are different.
#
# You may return the combinations in any order and the order of the numbers in each combination can be in any order.

from typing import List
class CombinationSum:
    def combinationSum(self,candidates: List[int],target : int):

        res = []
        subSet = []

        def dfs(i,curSum):

            if i >= len(candidates):
                return

            if curSum == target:
                res.append(subSet.copy())
                return
            subSet.append(candidates[i])
            dfs(i,curSum+candidates[i])
            subSet.pop()
            dfs(i+1,curSum)

        return res


