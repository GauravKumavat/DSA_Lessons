# You are given an 2-D array points where points[i] = [xi, yi] represents the coordinates of a point on an X-Y axis plane. You are also given an integer k.
#
# Return the k closest points to the origin (0, 0).
#
# The distance between two points is defined as the Euclidean distance (sqrt((x1 - x2)^2 + (y1 - y2)^2)).
#
# You may return the answer in any order.

import  heapq
from typing import List

class KClosestPointsToOrigin:
    def kclosetPointsToOrigin(self, points :List[List[int]] ,k: int):

        minHeap = []

        for x,y in points:
            minHeap.append([x*x+y*y , x,y])

        heapq.heapify(minHeap)
        res = []

        while k > 0:
            dist , x , y = minHeap.pop()
            res.append([x,y])
            k -= 1

        return res

classObj = KClosestPointsToOrigin()
classObj.kclosetPointsToOrigin([[1,2],[-2,2],[0,-3]], 2)

