"""
539 Minimum Time Difference

Given a list of 24-hour clock time points in "Hour:Minutes" format, find the minimum minutes difference between any two time points in the list.
Example 1:
Input: ["23:59","00:00"]
Output: 1
Note:
The number of time points in the given list is at least 2 and won't exceed 20000.
The input time is legal and ranges from 00:00 to 23:59.
"""
class Solution:
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        def getMinutes(time):
            return int(time[:2])*60 + int(time[3:])
        slots = [False]*(24*60+1)   # index is the minutes, value means if this time has appeared
        first, last = 2**31-1, -2**31
        for time in timePoints:
            minutes = getMinutes(time)
            if slots[minutes]:
                return 0
            else:
                # mark minutes in slots, and also update first and last
                slots[minutes] = True
                first = min(first, minutes)
                last = max(last, minutes)
        
        res = 24*60 + first - last  # calculate the difference between last and first
        prev = first
        for t in range(first+1, last+1):
            if slots[t]:
                res = min(res, t - prev)
                prev = t
        
        return res

    # my own solution by sorting timePoints, O(nlogn)
    def findMinDifference2(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        def getMinutes(time):
            return int(time[:2])*60 + int(time[3:])

        timePoints.sort()
        res, diff = 24*60, 0

        for i in range(1, len(timePoints)):
            diff = getMinutes(timePoints[i]) - getMinutes(timePoints[i-1])
            res = min(res, diff)

        # don't forget the difference between last and first time point
        res = min(res, 24*60 + getMinutes(timePoints[0]) - getMinutes(timePoints[-1]))

        return res

timePoints = ["23:59","00:00"]
print(Solution().findMinDifference(timePoints))