"""
630 Course Schedule III

There are n different online courses numbered from 1 to n. Each course has some duration(course length) t and closed on dth day. 
A course should be taken continuously for t days and must be finished before or on the dth day. You will start at the 1st day.

Given n online courses represented by pairs (t,d), your task is to find the maximal number of courses that can be taken.

Example:
Input: [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
Output: 3
Explanation: 
There're totally 4 courses, but you can take 3 courses at most:
First, take the 1st course, it costs 100 days so you will finish it on the 100th day, and ready to take the next course on the 101st day.
Second, take the 3rd course, it costs 1000 days so you will finish it on the 1100th day, and ready to take the next course on the 1101st day. 
Third, take the 2nd course, it costs 200 days so you will finish it on the 1300th day. 
The 4th course cannot be taken now, since you will finish it on the 3300th day, which exceeds the closed date.
Note:
The integer 1 <= d, t, n <= 10,000.
You can't take two courses simultaneously.
"""
# tags: greedy, interval
# why should we sort the intervals based on the end value in this problem?
from heapq import heappush, heappop
class Solution:
    # help from http://www.cnblogs.com/grandyang/p/7126289.html
    # greedy algorithm: sort the courses by the end time, iterate all courses, 
    # for each course, add during to priority queue, add during to start time and check if it meets end time requirement, if not, remove the longest duration course
    def scheduleCourse(self, courses):
        """
        :type courses: List[List[int]]
        :rtype: int
        """
        cur = 0
        courses.sort(key = lambda c: c[1])  # sort courses by the end time
        q = []

        for duration, endTime in courses:
            cur += duration
            heappush(q, -duration)
            if cur > endTime:
                cur += heappop(q)   # note that heap saves the negative duration
            
        return len(q)

    # my own wrong solution with priority queue
    # calculate each course's last start date (d-t+1) and sort the courses based on the last start date and during days
    # doesn't work for [[5,5],[4,6],[2,6]] which expects 2
    def scheduleCourse2(self, courses):
        """
        :type courses: List[List[int]]
        :rtype: int
        """
        a = []
        for t, d in courses:
            heappush(a, (d-t+1, t)) # bug fixed: should use d-t+1 because it is the correct beginning date 
        
        start, count = 1, 0
        while a:
            s, t = heappop(a)
            if s < start:
                break
            start += t
            count += 1
        
        return count
    
#courses = [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
courses = [[5,5],[4,6],[2,6]] # expected 2
print(Solution().scheduleCourse(courses))