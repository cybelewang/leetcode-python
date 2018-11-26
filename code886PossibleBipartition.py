"""
886 Possible Bipartition

Given a set of N people (numbered 1, 2, ..., N), we would like to split everyone into two groups of any size.

Each person may dislike some other people, and they should not go into the same group. 

Formally, if dislikes[i] = [a, b], it means it is not allowed to put the people numbered a and b into the same group.

Return true if and only if it is possible to split everyone into two groups in this way.

 

Example 1:

Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
Explanation: group1 [1,4], group2 [2,3]
Example 2:

Input: N = 3, dislikes = [[1,2],[1,3],[2,3]]
Output: false
Example 3:

Input: N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
Output: false
 

Note:

1 <= N <= 2000
0 <= dislikes.length <= 10000
1 <= dislikes[i][j] <= N
dislikes[i][0] < dislikes[i][1]
There does not exist i != j for which dislikes[i] == dislikes[j].
"""
# similar problems: 785 Is Graph Bipartite
from collections import defaultdict, deque
class Solution:
    # BFS solution using two colors (1 and -1 are two different groups, 0 means not grouped), similar to problem 785's solution
    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        colors = [0]*(N+1)
        graph = defaultdict(list)

        for a, b in dislikes:
            graph[a].append(b)
        
        for i in range(1, N+1):
            if colors[i] == 0:
                # BFS to color all nodes linked to node i
                colors[i] = 1
                q = deque([i])
                while q:
                    a = q.popleft()
                    for b in graph[a]:
                        if colors[b] == colors[a]:
                            return False
                        else:
                            colors[b] = - colors[a]
                            q.append(b)
        
        return True

#N, dislikes = 3, [[1,2],[1,3],[2,3]]
#N, dislikes = 5, [[1,2],[2,3],[3,4],[4,5],[1,5]]
N, dislikes = 4, [[1,2],[1,3],[2,4]]
print(Solution().possibleBipartition(N, dislikes))