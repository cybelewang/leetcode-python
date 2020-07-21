"""
210 Course Schedule II

There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

For example:

2, [[1,0]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1]

4, [[1,0],[2,0],[3,1],[3,2]]
There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. So one correct course order is [0,1,2,3]. Another correct ordering is[0,2,1,3].

Note:
The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
"""
import unittest
from collections import deque
class Solution:
    # use the similar code as in 207 Course Schedule with minor changes, see OneNote
    def findOrder_BFS(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = [[] for i in range(numCourses)]
        indegrees = [0 for i in range(numCourses)]

        for req in prerequisites:
            graph[req[1]].append(req[0])
            indegrees[req[0]] += 1
        
        queue = deque()
        queue.extend(i for i in range(numCourses) if indegrees[i] == 0)
        res = []

        while len(queue) > 0:
            src = queue.popleft()
            res.append(src)
            for dst in graph[src]:
                indegrees[dst] -= 1
                if indegrees[dst] == 0:
                    queue.append(dst)

        if any(indegrees):
            return []
        else:
            return res

    # DFS method
    def findOrder_DFS(self, numCourses, prerequisites):
        colors = [0]*numCourses # 0 - white - never visited, 1 - gray - visiting, 2 - black - visited
        # DFS to recurisvely iterate all nodes, return False if there is a cycle
        def dfs(node, graph, colors, res):
            if colors[node] == 2: return True
            if colors[node] == 1: return False
            colors[node] = 1
            for dst in graph[node]:
                if not dfs(dst, graph, colors, res):
                    return False
            colors[node] = 2
            res.append(node)
            return True

        # main
        # construct the graph
        graph = [set() for _ in range(numCourses)]
        for dst, src in prerequisites:
            graph[src].add(dst)

        res = []
        for node in range(numCourses):
            if not dfs(node, graph, colors, res):
                return []
        
        return res[::-1]

class Test(unittest.TestCase):
    def test_1(self):
        prerequisites = [[1, 0], [2, 1], [3, 2], [4, 3], [1, 4]]
        obj = Solution()
        self.assertEqual(obj.findOrder_BFS(5, prerequisites), [])
        self.assertEqual(obj.findOrder_DFS(5, prerequisites), [])

    def test_2(self):
        prerequisites = [[1,0],[2,0],[3,1],[3,2]]
        obj = Solution()
        self.assertTrue(obj.findOrder_BFS(4, prerequisites) in [[0,1,2,3], [0,2,1,3]])
        self.assertTrue(obj.findOrder_DFS(4, prerequisites) in [[0,1,2,3], [0,2,1,3]])

if __name__ == "__main__":
    unittest.main(exit = False)