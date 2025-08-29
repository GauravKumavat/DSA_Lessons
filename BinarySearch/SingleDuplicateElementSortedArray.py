# You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.
#
# Return the single element that appears only once.
#
# Your solution must run in O(log n) time and O(1) space.
#
#
#
# Example 1:
#
# Input: nums = [1,1,2,3,3,4,4,8,8]
# Output: 2
from typing import List

class SingleDuplicateElementSortedArray:
    def singleDupllicate(self,nums : List[int]):
        l,r = 0,len(nums)

        while l <= r:
            mid = (l+r)//2
            if ( (mid-1 < 0 or nums[mid-1] != nums[mid]) and (mid+1 == len(nums) or nums[mid] != nums[mid+1])):
                return nums[mid]

            leftSize = mid - 1 if nums[mid] == nums[mid-1] else mid
            if leftSize % 2:
                r = mid - 1
            else:
                l = mid+1


classObj = SingleDuplicateElementSortedArray()
