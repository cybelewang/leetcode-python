"""
310 Minimum Height Trees

For a undirected graph with tree characteristics, we can choose any node as the root. The result graph is then a rooted tree. Among all possible rooted trees, those with minimum height are called minimum height trees (MHTs). Given such a graph, write a function to find all the MHTs and return a list of their root labels.

Format
The graph contains n nodes which are labeled from 0 to n - 1. You will be given the number n and a list of undirected edges (each edge is a pair of labels).

You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

Example 1:

Given n = 4, edges = [[1, 0], [1, 2], [1, 3]]

        0
        |
        1
       / \
      2   3
return [1]

Example 2:

Given n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]

     0  1  2
      \ | /
        3
        |
        4
        |
        5
return [3, 4]

Note:

(1) According to the definition of tree on Wikipedia: “a tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.”

(2) The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.
"""
from collections import deque
class Solution:
    # BFS, start from all leaves in a queue, put their connected nodes into the next level queue and disconnect them. Keep doing BFS if there are nodes with more than 1 connection
    # Finally, one or two nodes (connected) are what we want
    # https://leetcode.com/problems/minimum-height-trees/discuss/76055/Share-some-thoughts
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n < 1:
            return []
        
        if n == 1:
            return [0]

        adj = [set() for _ in range(n)]   # adj[i] stores the nodes that connected to i
        for (first, second) in edges:
            adj[first].add(second)
            adj[second].add(first)
        
        leaves = [i for i in range(n) if len(adj[i]) == 1]

        # BFS        
        while n > 2:    # why n > 2 ? 
            n -= len(leaves)
            newLeaves = []
            for first in leaves:
                second = adj[first].pop()
                adj[second].remove(first)
                if len(adj[second]) == 1:   # this is very import! must check at this point, otherwise it won't work. see below comment.
                    newLeaves.append(second)

            leaves = newLeaves
            #leaves = [i for i in range(len(adj)) if len(adj[i]) == 1] # why this doesn't work? think about 1-2-3 

        return leaves

    # 2nd round solution on 5/13/2019
    def findMinHeightTrees2(self, n, edges):
        graph = [set() for _ in range(n)]   # graph[i] contains all nodes connected to node i
        for i, j in edges:
            graph[i].add(j)
            graph[j].add(i)
        
        q = deque(i for i in range(n) if len(graph[i])==1)
        while len(q) > 1:
            m = len(q)
            if m == 2:
                # check if the two nodes are connected, if so, the two nodes are what we want
                i, j = q[0], q[1]
                if i in graph[j] and j in graph[i]:
                    break

            for _ in range(m):
                i = q.popleft()
                for j in graph[i]:
                    #graph[i].remove(j) # should not modify a set during iteration
                    graph[j].remove(i)
                    if len(graph[j]) == 1:
                        q.append(j)
                graph[i].clear()
        
        return list(q)

obj = Solution()
n, edges = 8, [[0,1],[1,2],[2,3],[0,4],[4,5],[4,6],[6,7]]
n, edges = 3, [[0, 1], [1, 2]]
print(obj.findMinHeightTrees2(n, edges))