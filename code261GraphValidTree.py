"""
261 Graph Valid Tree

Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.
Example 1:
Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]]
Output: true
Example 2:
Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
Output: false
Note: you can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0,1] is the same as [1,0] and thus will not appear together in edges.
"""
import unittest
from collections import deque
class Solution:
    def validTree(self, n, edges):
        def find(root, i):
            while i != root[i]:
                i = root[i]
            return i
        
        root = [i for i in range(n)]
        # check if edges form a cycle
        for a, b in edges:
            p, q = find(root, a), find(root, b)
            if p == q:
                return False
            else:
                root[p] = q
        
        return len(edges) == n - 1 # check if all nodes are included in edges

    # BFS solution to find if cycle exists and if all nodes have been reached
    def validTree2(self, n, edges):
        """
        n: int
        edges: : List[List[int]]
        """
        # create undirected graph
        graph = [set() for _ in range(n)]
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)

        visited = [False]*n
        q = deque([0]) # start from any node, we should reach all other nodes in the graph
        visited[0] = True
        while q:
            src = q.popleft()
            for dst in list(graph[src]):
                if visited[dst]:
                    return False    # has cycles in graph
                else:
                    q.append(dst)
                    visited[dst] = True
                    # pitfall: don't forget to remove edge between src and dst!
                    graph[src].remove(dst)
                    graph[dst].remove(src)
                    
        # check if there are nodes unreached
        unvisited = [i for i in range(n) if not visited[i]]
        return len(unvisited) == 0

class Test(unittest.TestCase):
    def test_1(self):
        obj = Solution()
        edges = [[0,1], [0,2], [0,3], [1,4]]
        self.assertTrue(obj.validTree(5, edges))
    def test_2(self):
        obj = Solution()
        edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
        self.assertFalse(obj.validTree(5, edges))

if __name__ == "__main__":
    unittest.main(exit=False)