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
# tags: Dijkstra
# Dijkstra Algorithm - single source shortest-path tree algorithm
from heapq import heapify, heappush, heappop
from collections import defaultdict, deque
class Solution:
    # my own solution with BFS and priority queue
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        graph = defaultdict(lambda: defaultdict(int))
        for u, v, w in times:
            graph[u][v] = w
        
        q = [(0, K)]
        dist = [2**31-1]*(N + 1)
        dist[0] = 0
        dist[K] = 0
        while q:
            t, src = heappop(q)
            for dst in graph[src]:
                new_t = t + graph[src][dst]
                if dist[dst] > new_t:
                    dist[dst] = new_t
                    heappush(q, (new_t, dst))

        t = max(dist)
        return t if t < 2**31-1 else -1

    # Dijkstra solution with O(V^2) time complexity, V is the number of nodes
    # This will produce a shortest path tree (dist in this program) and each one represents the shortest path from the source
    def networkDelayTime_Dijkstra(self, times, N, K):
        INT_MAX = 2**31

        # dist[i] is the shortest distance from source to node i, initially set to INT_MAX except the source node
        dist = [INT_MAX]*(N+1)
        dist[0] = dist[K] = 0   # node 0 is a dummy node

        # set of all nodes
        Q = set(range(1, N+1))

        # prev list for path reconstruction between src and target
        prev = [None]*(N + 1)

        # create an adjacency matrix to represent the graph, to save space, we use nested dict
        edges = defaultdict(dict)
        for u, v, w in times:
            edges[u][v] = w

        while Q:
            # find node in Q with minimum dist
            u = None
            for node in Q:
                if u == None or dist[node] < dist[u]:
                    u = node
            
            Q.remove(u) # remove u from Q
            for v in edges[u]:
                if dist[v] > dist[u] + edges[u][v]:
                    dist[v] = dist[u] + edges[u][v]   # update the shortest path from source to v
                    prev[v] = u

        # reconstruct the shortest path from src to target
        print(prev)
        print(self.path(prev, 1, 2))
        res = max(dist)
        return -1 if res == INT_MAX else res

    # output the shortest path from start to end, if shortest path doesn't exist, return empty list
    def path(self, prev, start, end):
        res, u = [], end
        while u is not None:
            res.append(u)
            if u == start:
                break
            u = prev[u]
        if res and res[-1] != start:
            res.clear()
        
        return res[::-1]

    # Bellman-Ford algorithm
    # https://www.cnblogs.com/grandyang/p/8278115.html
    def networkDelayTime_BF(self, times, N, K):
        INT_MAX = 2**31 - 1
        dist = [INT_MAX]*(N+1) # dist[0] is dummy
        dist[0] = 0 # dist[0] is dummy
        dist[K] = 0

        for _ in range(N-1):
            for u, v, w in times:
                if dist[u] != INT_MAX:
                    dist[v] = min(dist[v], dist[u] + w)
        
        d = max(dist)
        return d if d != INT_MAX else -1
        
#times = [[1, 2, 1], [1, 3, 5], [2, 3, 1]]
#times = [[1,2,1],[2,3,1],[3,1,1]]
#times = [[1, 2, 1]]
#times = [[1,2,1],[2,3,7],[1,3,4],[2,1,2]]
times = [[1,4,1],[4,3,1],[3,2,1]]
obj = Solution()
print(obj.networkDelayTime_Dijkstra(times, 4, 1))
