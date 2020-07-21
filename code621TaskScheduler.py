"""
621 Task Scheduler

Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks.
Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.

However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n intervals that CPU are doing different tasks or just be idle.

You need to return the least number of intervals the CPU will take to finish all the given tasks.

Example 1:
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
Note:
The number of tasks is in the range [1, 10000].
The integer n is in the range [0, 100].
"""
# how to understand the example: between two 'A's there are at least 2 intervals ('B' and idle)
class Solution:
    # help from http://www.cnblogs.com/grandyang/p/7098764.html
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        count = [0]*26
        for char in tasks:
            count[ord(char) - ord('A')] += 1
        
        count.sort()
        i, mx = 25, count[25]
        while i > -1 and count[i] == mx:
            i -= 1
        
        # (mx-1)*(n+1) is the total length of repeating pattern without last repeating letter, for example, mx=3, n=2 will be A - - A - - [A], here [A] means omitting last letter
        # 25 - i is the length of most frequent task, for example, AB
        # Then we will fill other tasks into empty dashes, - , if overfilled, then no idles left and we take len(tasks)
        return max(len(tasks), (mx-1)*(n+1) + 25 - i)