"""
986 Interval List Intersections

Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

(Formally, a closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.  The intersection of two closed intervals is a set of real numbers that is either empty, or can be represented as a closed interval.  For example, the intersection of [1, 3] and [2, 4] is [2, 3].)

Example 1:
Input: A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
Reminder: The inputs and the desired output are lists of Interval objects, and not arrays or lists.

Note:

0 <= A.length < 1000
0 <= B.length < 1000
0 <= A[i].start, A[i].end, B[i].start, B[i].end < 10^9
"""
from Interval import *
class Solution:
    # https://leetcode.com/problems/interval-list-intersections/solution/
    # better to understand
    def intervalIntersection(self, A, B):    
        ans = []
        i = j = 0

        while i < len(A) and j < len(B):
            # Let's check if A[i] intersects B[j].
            # lo - the startpoint of the intersection
            # hi - the endpoint of the intersection
            lo = max(A[i].start, B[j].start)
            hi = min(A[i].end, B[j].end)
            if lo <= hi:
                ans.append(Interval(lo, hi))

            # Remove the interval with the smallest endpoint
            if A[i].end < B[j].end:
                i += 1
            else:
                j += 1

        return ans
    # my own solution, accepted
    def intervalIntersection2(self, A, B):
        """
        :type A: list[Interval]
        :type B: list[Interval]
        :rtype: list[Interval]
        """
        res, j = [], 0
        for a in A:
            # skip those ahead of interval a
            while j < len(B) and B[j].end < a.start:
                j += 1
            
            # get intersections
            k = j
            while k < len(B) and B[k].start <= a.end:
                res.append(Interval(max(a.start, B[k].start), min(a.end, B[k].end)))
                k += 1
        
        return res

    # 7/30/2020
    # put all cases into a single while loop
    def intervalIntersection3(self, A, B):
        i, j = 0, 0
        res = []
        while i < len(A) and j < len(B):
            if A[i][0] > B[j][1]: # B[j] on left of A[i]
                j += 1
            elif A[i][1] < B[j][0]: # B[j] on right of A[i]
                i += 1
            else: # A[i] and B[j] has intersection
                s, e = max(A[i][0], B[j][0]), min(A[i][1], B[j][1])
                res.append([s, e])
                if A[i][1] > B[j][1]: # advance pointer for interval with smaller end
                    j += 1
                else:
                    i += 1
        return res

#A, B = [], []   # expect []
#A, B = [], [Interval(1, 1)] # expect []
#A, B = [Interval(1, 1)], [] # expect []
#A, B = [Interval(1, 2), Interval(3, 5)], [Interval(0, 4)]   # expect [[1, 2], [3, 4]]
A, B = [Interval(0,2),Interval(5,10),Interval(13,23),Interval(24,25)], [Interval(1,5),Interval(8,12),Interval(15,24),Interval(25,26)]
print(Solution().intervalIntersection(A, B))
