"""
847 Shortest Path Visiting All Nodes

An undirected, connected graph of N nodes (labeled 0, 1, 2, ..., N-1) is given as graph.

graph.length = N, and j != i is in the list graph[i] exactly once, if and only if nodes i and j are connected.

Return the length of the shortest path that visits every node. You may start and stop at any node, you may revisit nodes multiple times, and you may reuse edges.

Example 1:

Input: [[1,2,3],[0],[0],[0]]
Output: 4
Explanation: One possible path is [1,0,2,0,3]
Example 2:

Input: [[1],[0,2,4],[1,3,4],[2],[1,2]]
Output: 4
Explanation: One possible path is [0,1,4,2,3]

Note:
1 <= graph.length <= 12
0 <= graph[i].length < graph.length
"""
from collections import deque
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        # BFS, (state, node)
        N = len(graph)
        
        target = (1 << N) - 1
        q, visited = deque(), set()
        for i in range(N):
            q.append((1 << i, i))
            visited.add((1 << i, i))
        
        steps = 0
        while q:
            size = len(q)
            for _ in range(size):
                state, src = q.popleft()
                if state == target:
                    return steps
                for dst in graph[src]:
                    new_state = state | (1 << dst)
                    if (new_state, dst) not in visited:
                        q.append((new_state, dst))
                        visited.add((new_state, dst))
            steps += 1
        return -1