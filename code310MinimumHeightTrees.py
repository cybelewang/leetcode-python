"""
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
class Solution:
    # BFS, start from all leaves in a queue, put their connected nodes into the next level queue and disconnect them. Keep doing BFS if there are nodes with more than 1 connection
    # Finally, the nodes with only 1 connection are what we want
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n < 1 or len(edges) < 1:
            return []

        count = [0]*n   # count[i] is the number of nodes connected to i
        link = [[] for i in range(n)]   # link[i] stores the nodes that connected to i
        for (first, second) in edges:
            link[first].append(second)
            count[first] += 1
            link[second].append(first)
            count[second] += 1
        
        queue = set()
        for i in range(n):
            if count[i] == 1:
                queue.add(i)

        # BFS        
        while max(count) > 1:
            next_queue = set()
            for first in queue:
                second = link[first][0]
                next_queue.add(second)
                link[first].remove(second)
                count[first] -= 1
                link[second].remove(first)
                count[second] -= 1
        
            queue = next_queue
        
        return list(queue)

obj = Solution()
edges = [[0,3], [1,3], [2,3], [3,4], [4,5], [5,7],[5,8], [5,6]]
print(obj.findMinHeightTrees(9, edges))