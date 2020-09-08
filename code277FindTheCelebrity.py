"""
277 Find the Celebrity

Suppose you are at a party with n people (labeled from 0 to n - 1) and among them, there may exist one celebrity. The definition of a celebrity is that all the other n - 1 people know him/her but he/she does not know any of them.

Now you want to find out who the celebrity is or verify that there is not one. The only thing you are allowed to do is to ask questions like: "Hi, A. Do you know B?" to get information of whether A knows B. You need to find out the celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).

You are given a helper function bool knows(a, b) which tells you whether A knows B. Implement a function int findCelebrity(n). There will be exactly one celebrity if he/she is in the party. Return the celebrity's label if there is a celebrity in the party. If there is no celebrity, return -1.

Example 1:
Input: graph = [
  [1,1,0],
  [0,1,0],
  [1,1,1]
]
Output: 1
Explanation: There are three persons labeled with 0, 1 and 2. graph[i][j] = 1 means person i knows person j, otherwise graph[i][j] = 0 means person i does not know person j. The celebrity is the person labeled as 1 because both 0 and 2 know him but 1 does not know anybody.

Example 2:
Input: graph = [
  [1,0,1],
  [1,1,0],
  [0,1,1]
]
Output: -1
Explanation: There is no celebrity.

Note:

The directed graph is represented as an adjacency matrix, which is an n x n matrix where a[i][j] = 1 means person i knows person j while a[i][j] = 0 means the contrary.
Remember that you won't have direct access to the adjacency matrix.
"""
# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    # See OneNote for explanation
    # time O(N), space O(N)
    def findCelebrity(self, n: int) -> int:
        @lru_cache(maxsize=None)
        def cachedKnows(a, b):
            return knows(a, b)
        
        candidate = 0
        for i in range(n):
            if i != candidate and cachedKnows(candidate, i):
                candidate = i
        
        for i in range(n):
            if i == candidate: continue
            if cachedKnows(candidate, i) or not cachedKnows(i, candidate):
                return -1
        
        return candidate

    # TLE solution because we use fixed celebrity check
    def findCelebrity_TLE(self, n: int) -> int:
        Q = set(range(n)) # possible celebrity
        while len(Q) > 1:
            x = Q.pop()
            Q.add(x)
            for i in range(n):
                if i != x:
                    if knows(i, x):
                        Q.discard(i)
                    else:
                        Q.discard(x)
        if not Q: return -1
        x = Q.pop()
        if sum(1 for i in range(n) if knows(i, x)) == n\
        and sum(1 for i in range(n) if knows(x, i)) == 1:
            return x
        else:
            return -1