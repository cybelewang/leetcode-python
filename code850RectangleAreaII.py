"""
850 Rectangle Area II

We are given a list of (axis-aligned) rectangles.  Each rectangle[i] = [x1, y1, x2, y2] , where (x1, y1) are the coordinates of the bottom-left corner, and (x2, y2) are the coordinates of the top-right corner of the ith rectangle.

Find the total area covered by all rectangles in the plane.  Since the answer may be too large, return it modulo 10^9 + 7.

Example 1:

Input: [[0,0,2,2],[1,0,2,3],[1,0,3,1]]
Output: 6
Explanation: As illustrated in the picture.
Example 2:

Input: [[0,0,1000000000,1000000000]]
Output: 49
Explanation: The answer is 10^18 modulo (10^9 + 7), which is (10^9)^2 = (-7)^2 = 49.
Note:

1 <= rectangles.length <= 200
rectanges[i].length = 4
0 <= rectangles[i][j] <= 10^9
The total area covered by all rectangles will never exceed 2^63 - 1 and thus will fit in a 64-bit signed integer.
"""
class Solution:
    # line sweep method, sweep y coordinates, time O(N^2*logN)
    # first put all events (y1, OPEN, x1, x2) and (y2, CLOSE, x1, x2) into events list, sort events
    # in each y, combined with pre_y, query the accumulated interval length of all (x1, x2) intervals between pre_y and y
    # calculate the area formed by pre_y and y, accumulated length of all (x1, x2) intervals 
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        OPEN, CLOSE = 0, 1
        events = []
        for x1, y1, x2, y2 in rectangles:
            events.append((y1, OPEN, x1, x2))
            events.append((y2, CLOSE, x1, x2))            
        events.sort()
        
        def query(intervals):
            # accumulation length of intervals
            ans = 0
            cur = -1
            for x1, x2 in intervals:
                cur = max(cur, x1)
                ans += max(0, x2 - cur)
                cur = max(cur, x2)
            return ans
        
        intervals = []
        pre_y = events[0][0]
        ans = 0
        for y, typ, x1, x2 in events:
            ans += query(intervals)*(y-pre_y)
            if typ == OPEN:
                intervals.append((x1, x2))
                intervals.sort()
            else:
                intervals.remove((x1, x2))
            pre_y = y
        
        return ans % (10**9 + 7)