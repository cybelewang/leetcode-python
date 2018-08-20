"""

In this problem, a tree is an undirected graph that is connected and has no cycles.

The given input is a graph that started as a tree with N nodes (with distinct values 1, 2, ..., N), with one additional edge added. 
The added edge has two different vertices chosen from 1 to N, and was not an edge that already existed.

The resulting graph is given as a 2D-array of edges. Each element of edges is a pair [u, v] with u < v, that represents an undirected edge connecting nodes u and v.

Return an edge that can be removed so that the resulting graph is a tree of N nodes. 
If there are multiple answers, return the answer that occurs last in the given 2D-array. The answer edge [u, v] should be in the same format, with u < v.

Example 1:
Input: [[1,2], [1,3], [2,3]]
Output: [2,3]
Explanation: The given undirected graph will be like this:
  1
 / \
2 - 3
Example 2:
Input: [[1,2], [2,3], [3,4], [1,4], [1,5]]
Output: [1,4]
Explanation: The given undirected graph will be like this:
5 - 1 - 2
    |   |
    4 - 3
Note:
The size of the input 2D-array will be between 3 and 1000.
Every integer represented in the 2D-array will be between 1 and N, where N is the size of the input array.

Update (2017-09-26):
We have overhauled the problem description + test cases and specified clearly the graph is an undirected graph. For the directed graph follow up please see Redundant Connection II). We apologize for any inconvenience caused.

"""
# similar problems: 261 Graph Valid Tree; 
class Solution:
    # Union Find solution http://www.cnblogs.com/grandyang/p/7628977.html
    # O(N) space
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        def find(root, i):
            """
            find the largest "root" node which is connected to i
            """
            while root[i] != -1:
                i = root[i]

            return i

        N = len(edges)
        root = [-1]*(N+1)

        for u, v in edges:
            x, y = find(root, u), find(root, v)
            if x == y:  # shared the root, must be connected
                return [u, v]
            root[x] = y # bug fixed: previously was root[u] = v

        return []

    # Wrong solution because it doesn't link the nodes if they are not directly connected
    # my brutal force solution with O(N^2) space
    def findRedundantConnection2(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        N = len(edges)
        connected = [set() for _ in range(N)]   # connected[i] is a set containing all nodes connected to (i+1)

        for u, v in edges:
            if v in connected[u-1]: # we should not check like this. We should use DFS to check if u and v are connected. See findRedundantConnection3
                return [u, v]
            
            for p in connected[u-1]:
                connected[p-1].add(v)
                connected[v-1].add(p)

            connected[u-1].add(v)
            connected[v-1].add(u)
        
        return []

    # correct DFS solution, revised from findRedundantConnection2
    def findRedundantConnection3(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        N = len(edges)
        connected = [set() for _ in range(N)]   # connected[i] is a set containing all nodes connected to (i+1)

        def dfs(u, v, visited):
            """
            check if u and v are connected
            visited: a set stores the visited nodes
            """
            if u == v:
                return True

            if u not in visited:
                visited.add(u)
                return any(dfs(p, v, visited) for p in connected[u-1])

            return False

        for u, v in edges:            
            visited = set()
            if dfs(u, v, visited):
                return [u, v]

            connected[u-1].add(v)
            connected[v-1].add(u)        

        return []

edges = [[1,4],[3,4],[1,3], [1,2], [4,5]] # expected: [1,3]
print(Solution().findRedundantConnection3(edges))