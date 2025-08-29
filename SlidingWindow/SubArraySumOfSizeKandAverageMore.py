# You are given an array of integers arr and two integers k and threshold, return the number of sub-arrays of size k and average greater than or equal to threshold.
#
# Example 1:
#
# Input: arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
#
# Output: 3
from typing import List

class SubArraySumOfSizeKandAverageMore:
    def subarrySum(self,arr: List[int], k : int , threshold : int):
        res = 0
        windowSum = sum(arr[:k-1])

        for l in range(len(arr) - k +1):
            windowSum += arr[l + k - 1]
            if windowSum/k >= threshold:
                res += 1
            windowSum -= arr[l]
        return res



classOb =  SubArraySumOfSizeKandAverageMore()
print(classOb.subarrySum([1,2,3,4,5,6],3,4))