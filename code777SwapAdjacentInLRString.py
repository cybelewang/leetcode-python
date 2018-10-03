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
class Solution:
    # my own solution
    # remove all X's and compare if the remaining strings are equal - this is wrong, for example, we cannot make "RLX" and "XRL" equal
    # R can move to right along X, until stopped by a L
    # L can move to left along X, until stopped by a R
    def canTransform(self, start, end):
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

start = "XXRXXLXXXX"
end = "XXXXRXXLXX"
print(Solution().canTransform(start, end))