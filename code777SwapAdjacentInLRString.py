"""
777 Swap Adjacent in LR String

In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL", a move consists of either replacing one occurrence of "XL" with "LX", 
or replacing one occurrence of "RX" with "XR". Given the starting string start and the ending string end, 
return True if and only if there exists a sequence of moves to transform one string to the other.

Example:

Input: start = "RXXLRXRXL", end = "XRLXXRRLX"
Output: True
Explanation:
We can transform start to end following these steps:
RXXLRXRXL ->
XRXLRXRXL ->
XRLXRXRXL ->
XRLXXRRXL ->
XRLXXRRLX
Note:

1 <= len(start) = len(end) <= 10000.
Both start and end will only consist of characters in {'L', 'R', 'X'}.
"""
# the relative sequence of 'R' and 'L' between start and end are the same
# understanding the problem correctly, the problem requires to transform from start to end, not from end to start, so the result of case start = "XR" and end = "RX" is false
# this implies that if start[i] == end[j] == 'R', then i <= j; if start[i] == end[j] == 'L', then i >= j
class Solution:
    # http://www.cnblogs.com/grandyang/p/9001474.html
    def canTransform(self, start, end):
        cntR, cntL, n = 0, 0, len(start)
        for i in range(n):
            if start[i] == 'R': cntR += 1   # start's 'R' must not be in the right of end's 'R', so we count 'R' in start first
            if end[i] == 'L': cntL += 1 # end's 'L' must not be in the left of start's 'L', so we count 'L' in end first
            if start[i] == 'L': cntL -= 1
            if end[i] == 'R': cntR -= 1
            if cntR < 0 or cntL < 0 or cntL*cntR != 0:  # cntR >= 0, cntL >= 0, but they cannot be both > 0
                return False
        
        return cntL == 0 and cntR == 0

    def canTransform2(self, start, end):
        i, j, n = 0, 0, len(start)
        while i < n or j < n:
            if i < n and start[i] == 'X':
                i += 1
            elif j < n and end[j] == 'X':
                j += 1
            elif i < n and j < n and ((start[i] == end[j] == 'R' and i <= j) or (start[i]==end[j]=='L' and i >=j)): # added the relative sequence requirement based on my own solution
                i += 1
                j += 1
            else:
                return False

        return True

    # my own solution
    # remove all X's and compare if the remaining strings are equal - this is wrong, for example, we cannot transform "XR" to "RX" because 'R' in start cannot move to right
    # R can move to right along X, until stopped by a L
    # L can move to left along X, until stopped by a R
    def canTransform_Wrong(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        i, j, n = 0, 0, len(start)
        while i < n or j < n:
            if i < n and start[i] == 'X':
                i += 1
            elif j < n and end[j] == 'X':
                j += 1
            elif i < n and j < n and start[i] == end[j]:
                i += 1
                j += 1
            else:
                return False

        return True

#start, end = "XXRXXLXXXX", "XXXXRXXLXX"
#start, end = "RXXLRXRXL", "XRLXXRRLX"
start, end = "RLX", "XRL"
print(Solution().canTransform(start, end))