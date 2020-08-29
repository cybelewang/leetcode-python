"""
1245 Tree Diameter

Given an undirected tree, return its diameter: the number of edges in a longest path in that tree.

The tree is given as an array of edges where edges[i] = [u, v] is a bidirectional edge between nodes u and v.  Each node has labels in the set {0, 1, ..., edges.length}.

Example 1:
Input: edges = [[0,1],[0,2]]
Output: 2
Explanation: 
A longest path of the tree is the path 1 - 0 - 2.

Example 2:
Input: edges = [[0,1],[1,2],[2,3],[1,4],[4,5]]
Output: 4
Explanation: 
A longest path of the tree is the path 3 - 2 - 1 - 4 - 5.

Constraints:
0 <= edges.length < 10^4
edges[i][0] != edges[i][1]
0 <= edges[i][j] <= edges.length
The given edges form an undirected tree.
"""
from collections import defaultdict
class Solution:
    # similar to 543 Diameter of Binary Tree, use DFS to return the single longest edges
    # in each DFS, update largest two depths
    def treeDiameter(self, edges: List[List[int]]) -> int:
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
            
        self.res = 0
        def dfs(root):
            first, second = 0, 0 # first and second largest depth
            for nei in graph[root]:
                graph[nei].remove(root)
                d = dfs(nei)
                if d > first:
                    first, second = d, first
                elif d > second:
                    second = d
            
            if len(graph[root]) == 0:
                return 0
            elif len(graph[root]) == 1:
                self.res = max(self.res, 1 + first)
            else:
                self.res = max(self.res, 2 + first + second)
            
            return 1 + first
        
        dfs(0)
        return self.res

    # DFS but sort the children depth
    def treeDiameter2(self, edges: List[List[int]]) -> int:
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
            
        self.res = 0
        def dfs(root):
            children = []
            for nei in graph[root]:
                graph[nei].remove(root)
                children.append(dfs(nei))
            
            children.sort(reverse = True)
            if len(children) == 0:
                return 0
            elif len(children) == 1:
                self.res = max(self.res, 1 + children[0])
            else:
                self.res = max(self.res, 2 + sum(children[:2]))
            
            return 1 + children[0]
        
        dfs(0)
        return self.res