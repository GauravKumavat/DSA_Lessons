# You are given an integer array nums where nums[i] represents the amount of money the ith house has. The houses are arranged in a circle, i.e. the first house and the last house are neighbors.
#
# You are planning to rob money from the houses, but you cannot rob two adjacent houses because the security system will automatically alert the police if two adjacent houses were both broken into.
#
# Return the maximum amount of money you can rob without alerting the police.
#
# Example 1:
#
# Input: nums = [3,4,3]
#
# Output: 4

from typing import List

class Robber_2:
    def findRobber(self, nums : List[int]):
        if len(nums) == 1:
            return nums[0]
        return max(self.helper(nums[1:]),
               self.helper(nums[:-1]))

    def dfs(self, nums : List[int]):

        dp = [0] * len(nums)

        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i]+dp[i-2])

        return dp[-1]