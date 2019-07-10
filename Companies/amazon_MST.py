"""
Minimum Spanning Tree

The cost of the spanning tree is the sum of the weights of all the edges in the tree. There can be many spanning trees. 
Minimum spanning tree is the spanning tree where the cost is minimum among all the spanning trees. There also can be many minimum spanning trees.

Applications: Connect all cities with least cost
"""
class Solution:
    def mst(self, numNodes, graph):
        """
        :type numNodes: int - number of nodes in this graph
        :type graph: list[int] - first node, second node, edge weight
        :rtype: int - the minimum cost
        """
        # union find function
        def unionfind(root, id):
            while id != root[id]:
                id = root[id]
            
            return id
        
        root = [i for i in range(numNodes)] # root list for union find
        graph.sort(key = lambda x: (x[2], x[0], x[1]))  # sort the graph based on the edge weight
        res = 0

        for x, y, weight in graph:
            p, q = unionfind(root, x), unionfind(root, y)   # union find the root nodes for x and y
            if p != q:
                res += weight
                root[p] = root[q]   # union two disjoint sets
        
        return res

graph = [[0, 1, 2], [0, 4, 4], [1, 2, 6], [1, 4, 3], [2, 3, 7], [2, 4, 5], [3, 4, 1]]
print(Solution().mst(5, graph))