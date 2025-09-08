# Given an array of intervals where intervals[i] = [start_i, end_i], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
#
# You may return the answer in any order.
#
# Note: Intervals are non-overlapping if they have no common point. For example, [1, 2] and [3, 4] are non-overlapping, but [1, 2] and [2, 3] are overlapping.
#
# Example 1:
#
# Input: intervals = [[1,3],[1,5],[6,7]]
#
# Output: [[1,5],[6,7]]

from typing import List

class MergeIntervals:
    def merge(self, intervals: List[List[int]]):

        intervals.sort(key = lambda i : i[0])
        output = [intervals[0]]

        for start ,end  in intervals[1:]:
            laststart,lastEnd = output[-1]

            if lastEnd >= start:
                output[-1][1] = max(lastEnd,end)
            else:
                output.append([start,end])

        return output
