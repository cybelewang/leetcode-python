"""
743 Network Delay Time

There are N network nodes, labelled 1 to N.

Given times, a list of travel times as directed edges times[i] = (u, v, w), where u is the source node, v is the target node, and w is the time it takes for a signal to travel from source to target.

Now, we send a signal from a certain node K. How long will it take for all nodes to receive the signal? If it is impossible, return -1.

Note:
N will be in the range [1, 100].
K will be in the range [1, N].
The length of times will be in the range [1, 6000].
All edges times[i] = (u, v, w) will have 1 <= u, v <= N and 1 <= w <= 100.
"""
from heapq import heappush, heappop
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        # convert times to a graph (type dict, key is the source node, value is a list of tuple (dst node, time))
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        
        visited = [False]*(1+N)
        q = [(0, K)]    # priority queue implemented by heapq
        remains, t = N, 0
        while q and remains:
            t, src = heappop(q)
            visited[src] = True
            remains -= 1
            for dst, time in graph[src]:
                if not visited[dst]:
                    heappush(q, (t+time, dst))
                    # bug fixed: below commented codes should not be here
                    # visited[src] = True
                    # remains -= 1
        return -1 if remains else t

times = [[1, 2, 1], [1, 3, 5], [2, 3, 1]]
#times = [[1,2,1],[2,3,1],[3,1,1]]
#times = [[1, 2, 1]]
obj = Solution()
print(obj.networkDelayTime(times, 3, 1))