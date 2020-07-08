"""
802 Find Eventual Safe States

In a directed graph, we start at some node and every turn, walk along a directed edge of the graph.  If we reach a node that is terminal (that is, it has no outgoing directed edges), we stop.

Now, say our starting node is eventually safe if and only if we must eventually walk to a terminal node.  More specifically, there exists a natural number K so that for any choice of where to walk, we must have stopped at a terminal node in less than K steps.

Which nodes are eventually safe?  Return them as an array in sorted order.

The directed graph has N nodes with labels 0, 1, ..., N-1, where N is the length of graph.  The graph is given in the following form: graph[i] is a list of labels j such that (i, j) is a directed edge of the graph.

Example:
Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
Output: [2,4,5,6]
Here is a diagram of the above graph.

Illustration of graph

Note:

graph will have length at most 10000.
The number of edges in the graph will not exceed 32000.
Each graph[i] will be a sorted list of different integers, chosen within the range [0, graph.length - 1].
"""
from collections import deque, defaultdict
class Solution:
    # help from http://www.cnblogs.com/grandyang/p/9319966.html
    # BFS starting from the terminal nodes (nodes whose out-degree are 0), expanding to their source nodes
    # When visiting source nodes, disconnect their connections and reduce the out degrees, if the out-degree becomes 0, mark the node as safe, also add to queue
    def eventualSafeNodes_BFS(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        n = len(graph)
        g, revg = [set() for _ in range(n)], [set() for _ in range(n)]
        safe, q = [False]*n, deque()

        for i in range(n):
            if not graph[i]:
                q.append(i)
            for j in graph[i]:
                g[i].add(j)
                revg[j].add(i)

        while q:
            j = q.popleft()
            safe[j] = True
            for i in revg[j]:
                g[i].discard(j)
                if not g[i]:
                    q.append(i)
        
        return [i for i in range(n) if safe[i]]

    # Similar to 207 Course Schedule, but use out degrees instead of in degrees
    def eventualSafeNodes2(self, graph):
        n = len(graph)
        revG = defaultdict(set) # reverse graph with reversed edges, for easy to get src from dst
        outdegrees = [0]*n
        for src in range(n):
            outdegrees[src] = len(graph[src])
            for dst in graph[src]:
                revG[dst].add(src)

        q = deque([i for i in range(n) if outdegrees[i] == 0])
        while q:
            dst = q.popleft()
            for src in revG[dst]:
                outdegrees[src] -= 1
                if outdegrees[src] == 0:
                    q.append(src)

        return [i for i in range(n) if outdegrees[i] == 0]

    def eventualSafeNodes_DFS(self, graph):
        def dfs(graph, i, color):
            """
            return True if node i is eventually a safe node
            """
            if color[i] > 0:
                return color[i] == 2
            
            color[i] = 1    # gray, visiting neighboring nodes
            for j in graph[i]:
                if color[j] == 2:
                    continue
                if color[j] == 1 or not dfs(graph, j, color):
                    return False
            color[i] = 2    # black, completing visiting

            return True
        
        # main
        n = len(graph)
        color = [0]*n

        return [i for i in range(n) if dfs(graph, i, color)]

    # WRONG solution, this problem tests out degrees, not in degrees
    # IN degrees + BFS to detect cycles, the nodes not in a cycle (indegree of 0) are the required nodes
    # The mistake is that nodes with non-zero indegrees are not necessarily in cycle. See test case.
    def eventualSafeNodes_Cycles(self, graph):
        N = len(graph)
        indegrees = [0]*N
        for a, dsts in enumerate(graph):
            for b in dsts:
                indegrees[b] += 1
        
        q = deque([i for i in range(N) if indegrees[i] == 0])
        print(q)
        while q:
            a = q.popleft()
            for b in graph[a]:
                indegrees[b] -= 1
                if indegrees[b] == 0:
                    q.append(b)
        
        print(indegrees)
        return [i for i in range(N) if indegrees[i] == 0]

graph = [[1,2],[2,3],[5],[0],[5],[],[]]
print(Solution().eventualSafeNodes2(graph))