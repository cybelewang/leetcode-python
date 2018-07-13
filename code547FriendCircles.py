"""
There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature. For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C. And we defined a friend circle is a group of students who are direct or indirect friends.

Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. And you have to output the total number of friend circles among all the students.

Example 1:
Input: 
[[1,1,0],
 [1,1,0],
 [0,0,1]]
Output: 2
Explanation:The 0th and 1st students are direct friends, so they are in a friend circle. 
The 2nd student himself is in a friend circle. So return 2.
Example 2:
Input: 
[[1,1,0],
 [1,1,1],
 [0,1,1]]
Output: 1
Explanation:The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends, 
so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, so return 1.
Note:
N is in range [1,200].
M[i][i] = 1 for all students.
If M[i][j] = 1, then M[j][i] = 1.
"""
from collections import deque
class Solution:
    # my 2nd trial
    # create a set to store students not processed
    # iterate all students, for each student in the set, use BFS to process all friends, and remove friends from the set
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        N, circle = len(M), 0
        unvisited = set(range(N))
        q = deque()
        for i in range(N):
            # ignore those visited because they belong to existing circles
            if i in unvisited:
                unvisited.remove(i)
                circle += 1
                q.append(i)
                while q:
                    host = q.popleft()
                    for friend in range(host+1, N):
                        if M[host][friend]:
                            unvisited.remove(friend)
                            q.append(friend)
                
        return circle


    # 1st trial, iterate all cells of M, for each connection, use BFS to color indirect connections. The result is wrong because we missed those without friends
    def findCircleNum2(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        N = len(M)
        circle = 1  # id of the friend circle
        q = deque()
        for i in range(N):
            for j in range(i+1, N):
                if M[i][j] == 1:
                    circle += 1
                    q.append(i)
                    q.append(j)
                    M[i][j] = circle
                    while q:
                        host = q.popleft()
                        for k in range(host+1, N):
                            if M[host][k] == 1:
                                M[host][k] = circle
                                q.append(k)

        return circle - 1

M = [[1, 1, 0], [0, 1, 1], [0, 1, 1]]
print(Solution().findCircleNum(M))