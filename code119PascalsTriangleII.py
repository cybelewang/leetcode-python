"""
119 Pascal's Triangle II

Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?
"""

# Key is to use a temp variable to save the element value before adding itself with the previous one.
class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex < 0:
            return []

        build = [0 for i in range(rowIndex + 1)]    # Initialize the result array
        build[0] = 1

        for row in range(1, rowIndex + 1):
            pre = build[0]  # this is the "original" previous value
            for i in range(1, row + 1):
                temp = build[i] # temporarily save the "original" value of build[i] because it will be added to the next element in the next step
                build[i] += pre
                pre = temp  # update the "pre" value to current, so it can be added to the next element
            build[row] = 1  # append "1" at the end
        
        return build
    # best solution from leetcode: add from end
    def getRow2(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res=[1]*(rowIndex+1)
        for i in range(1,rowIndex):
            for j in range(i,0,-1):
                res[j]=res[j]+res[j-1]
        return res


obj = Solution()
print(obj.getRow2(2))
print(obj.getRow2(3))