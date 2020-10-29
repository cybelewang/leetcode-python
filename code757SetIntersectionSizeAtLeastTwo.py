"""
757 Set Intersection Size At Least Two

An integer interval [a, b] (for integers a < b) is a set of all consecutive integers from a to b, including a and b.

Find the minimum size of a set S such that for every integer interval A in intervals, the intersection of S with A has size at least 2.

Example 1:
Input: intervals = [[1, 3], [1, 4], [2, 5], [3, 5]]
Output: 3
Explanation:
Consider the set S = {2, 3, 4}.  For each interval, there are at least 2 elements from S in the interval.
Also, there isn't a smaller size set that fulfills the above condition.
Thus, we output the size of this set, which is 3.
Example 2:
Input: intervals = [[1, 2], [2, 3], [2, 4], [4, 5]]
Output: 5
Explanation:
An example of a minimum sized set is {1, 2, 3, 4, 5}.
Note:

intervals will have length in range [1, 3000].
intervals[i] will have length 2, representing some integer interval.
intervals[i][j] will be an integer in [0, 10^8].
"""
class Solution:
    # https://www.cnblogs.com/grandyang/p/8503476.html
    def intersectionSizeTwo(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        # sort the intervals based on (end, -start)
        # maintain a array to hold the numbers in set
        # if a <= last second number, skip this interval
        # if a == last number, append b to array (+1)
        # if a > last number, append b-1, b to array for possible overlap (+2)
        # if last second number < a < last number, append b to array (+1)
        intervals.sort(key = lambda x : (x[1], -x[0]))
        s = [-1, -1]
        for a, b in intervals:
            if a <= s[-2]: continue
            if a > s[-1]:
                s.append(b-1)
            s.append(b)
        return len(s) - 2     
    # O(1) space because we only use last and last_second
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : (x[1], -x[0]))
        last, last_second = -1, -1
        ans = 0
        for a, b in intervals:
            if a <= last_second: continue
            if a > last:
                ans += 1
                last_second, last = last, b-1
            last_second, last = last, b
            ans += 1
        return ans  