"""
785 Is Graph Bipartite?

Given an undirected graph, return true if and only if it is bipartite.

Recall that a graph is bipartite if we can split it's set of nodes into two independent subsets A and B such that every edge in the graph has one node in A and another node in B.

The graph is given in the following form: graph[i] is a list of indexes j for which the edge between nodes i and j exists.  Each node is an integer between 0 and graph.length - 1.  There are no self edges or parallel edges: graph[i] does not contain i, and it doesn't contain any element twice.

Example 1:
Input: [[1,3], [0,2], [1,3], [0,2]]
Output: true
Explanation: 
The graph looks like this:
0----1
|    |
|    |
3----2
We can divide the vertices into two groups: {0, 2} and {1, 3}.
Example 2:
Input: [[1,2,3], [0,2], [0,1,3], [0,2]]
Output: false
Explanation: 
The graph looks like this:
0----1
| \  |
|  \ |
3----2
We cannot find a way to divide the set of nodes into two independent subsets.
"""
class Solution:
    def isBipartite_DFS(self, graph):
        def dfs(graph, colors, i, color):
            if colors[i] == 0:
                colors[i] = color
                return all(dfs(graph, colors, j, -color) for j in graph[i])
            else:
                return colors[i] == color

        N = len(graph)
        colors = [0]*N  # 0 means not colored, 1 and -1 mean two different colors
        return dfs(graph, colors, 0, 1)

    #def isBipartite_BFS(self, graph):
        

    # my own solution using adjacent matrix, and any two rows must be either equal or complementation
    # space O(N^2)
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        N = len(graph)
        if N < 2:
            return False

        matrix = [[0]*N for _ in range(N)]  # adjacent matrix, 0 means no connection, and 1 means connection

        for j in graph[0]:  # create first row
            matrix[0][j] = 1

        for i in range(1, N):   # update other rows and compare with first row, must be either equal or complementation
            for j in graph[i]:
                matrix[i][j] = 1
            diff = matrix[i][0] ^ matrix[0][0]
            for j in range(N):
                if matrix[0][j] != (matrix[i][j] ^ diff):
                    return False
        
        return True

#graph = [[1,2,3], [0,2], [0,1,3], [0,2]]
#graph = [[1],[0,3],[3],[1,2]]
graph = [[],[2,4,6],[1,4,8,9],[7,8],[1,2,8,9],[6,9],[1,5,7,8,9],[3,6,9],[2,3,4,6,9],[2,4,5,6,7,8]]
print(Solution().isBipartite(graph))