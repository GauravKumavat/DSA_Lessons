# You are given a binary array nums.
#
# You can do the following operation on the array any number of times (possibly zero):
#
# Choose any 3 consecutive elements from the array and flip all of them.
# Flipping an element means changing its value from 0 to 1, and from 1 to 0.
#
# Return the minimum number of operations required to make all elements in nums equal to 1. If it is impossible, return -1.

from typing import List

class MinimumElementFlipToMakeArrayOne:
    def minElementToMakeArrayOne(self,nums: List[int]):

        def flip(i):
            if nums[i]:
                nums[i] = 0
            else:
                nums[i] = 1


        res = 0
        for i in range(len(nums)-2):
            if nums[i] == 0:
                flip(i)
                flip(i+1)
                flip(i+2)
                res += 1

        if not nums[-1]  or not nums[-2]:
            return -1

        return res


