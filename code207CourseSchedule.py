"""
207 Course Schedule

There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

For example:

2, [[1,0]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.

2, [[1,0],[0,1]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

Note:
The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
"""
from collections import deque
class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = [[] for i in range(numCourses)] # adjacency list graph[i] contains all the destinations starting from i
        indegrees = [0 for i in range(numCourses)] # in degrees of course i

        for req in prerequisites:
            graph[req[1]].append(req[0])    # append all destination course req[0] into source course req[1]'s list
            indegrees[req[0]] += 1  # the in degree of the destination increase by 1
        
        queue = deque()
        queue.extend(i for i in range(numCourses) if indegrees[i] == 0)

        while len(queue) > 0:
            src = queue.popleft()
            for dst in graph[src]:
                indegrees[dst] -= 1
                if indegrees[dst] == 0:
                    queue.append(dst)
        
        print(indegrees)
        return not any(indegrees)

prerequisites = [[1, 0], [2, 1], [3, 2], [4, 3], [1, 4]]
obj = Solution()
print(obj.canFinish(5, prerequisites))