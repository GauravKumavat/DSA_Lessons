# You are given a network of n directed nodes, labeled from 1 to n. You are also given times, a list of directed edges where times[i] = (ui, vi, ti).
#
# ui is the source node (an integer from 1 to n)
# vi is the target node (an integer from 1 to n)
# ti is the time it takes for a signal to travel from the source to the target node (an integer greater than or equal to 0).
# You are also given an integer k, representing the node that we will send a signal from.
#
# Return the minimum time it takes for all of the n nodes to receive the signal. If it is impossible for all the nodes to receive the signal, return -1 instead.


from typing import List
import collections
import heapq

class NetworkDelayTime:
    def minTime(self,times : List[List[int]],n: int, k : int):

        edges = collections.defaultdict(list)

        for u,v,w in times:
            edges[u].append((v,w))

        t=0
        visit = set()
        minHeap = [(0,k)]

        while minHeap:
            w,node = minHeap.pop()

            if node in visit:
                continue
            visit.add(node)
            t = max(t,w)

            for nei in edges[node]:
                node1,w2  = nei
                heapq.heappush(minHeap,(w+w2,node1))


        return t if len(visit) == n else -1
