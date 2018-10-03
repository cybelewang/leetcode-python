"""
787 Cheapest Flights Within K Stops

There are n cities connected by m flights. Each fight starts from city u and arrives at v with a price w.

Now given all the cities and fights, together with starting city src and the destination dst, your task is to find the cheapest price from src to dst with up to k stops. 
If there is no such route, output -1.

Example 1:
Input: 
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 1
Output: 200
Explanation: 
The graph looks like this:


The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as marked red in the picture.
Example 2:
Input: 
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 0
Output: 500
Explanation: 
The graph looks like this:


The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as marked blue in the picture.
Note:

The number of nodes n will be in range [1, 100], with nodes labeled from 0 to n - 1.
The size of flights will be in range [0, n * (n - 1) / 2].
The format of each flight will be (src, dst, price).
The price of each flight will be in the range [1, 10000].
k is in the range of [0, n - 1].
There will not be any duplicated flights or self cycles.
"""
from collections import defaultdict, deque
class Solution:
    # my own BFS solution
    def findCheapestPrice_BFS(self, n, flights, src, dst, K):
        edges = defaultdict(dict)
        for u, v, p in flights:
            edges[u][v] = p
        
        INT_MAX = 2**31 - 1
        prices = [INT_MAX]*n
        prices[src] = 0

        q = deque([src])
        while q and K > -1:
            m = len(q)
            for _ in range(m):
                i = q.popleft()
                for j in edges[i]:
                    if prices[i] + edges[i][j] < prices[j]:
                        prices[j] = prices[i] + edges[i][j]
                        q.append(j)
            
            K -= 1
        
        return -1 if prices[dst] == INT_MAX else prices[dst]

    def findCheapestPrice_DFS(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        edges = defaultdict(dict)
        for u, v, p in flights:
            edges[u][v] = p
        self.res = 2**31 - 1

        def dfs(i, k, p):
            if k > K + 1:
                return
            if i == dst:
                self.res = min(self.res, p)
                return
            for j in edges[i]:
                dfs(j, k+1, p + edges[i][j])

        dfs(src, 0, 0)

        return -1 if self.res == 2**31 - 1 else self.res

    # Bellman Ford algorithm from http://www.cnblogs.com/grandyang/p/9109981.html
    def findCheapestPrice(self, n, flights, src, dst, K):
        INT_MAX = 2**31 - 1
        dp = [[INT_MAX]*n for _ in range(K+2)]  # dp[i][j] is the lowest price flying i times to location j
        dp[0][src] = 0
        for i in range(1, K+2):
            dp[i][src] = 0
            for u, v, p in flights:
                dp[i][v] = min(dp[i][v], dp[i-1][u] + p)    # minimum betwee current lowest price, and last location + price from last location to this

        return -1 if dp[K+1][dst] >= INT_MAX else dp[K+1][dst]

n, src, dst, K = 3, 0, 2, 1
flights = [[0,1,100],[1,2,100],[0,2,500]]
print(Solution().findCheapestPrice(n, flights, src, dst, K))