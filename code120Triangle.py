"""
120 Triangle

Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.

"""

# Use backward adding method: curr = curr + min(upleft, upright)
class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0

        if len(triangle) == 1:
            return triangle[0][0]

        res = 2**31 - 1
        for i in range(1, len(triangle)):
            for (j, num) in enumerate(triangle[i]):
                upLeft, upRight = j - 1, j
                if upLeft < 0:
                    triangle[i][j] += triangle[i-1][upRight]
                elif upRight > i - 1:
                    triangle[i][j] += triangle[i-1][upLeft]
                else:
                    triangle[i][j] += min(triangle[i-1][upLeft], triangle[i-1][upRight])
                
                if i == len(triangle) - 1:
                    res = min(res, triangle[i][j])
        
        return res
    
    # 2nd round solution on 12/11/2018
    # back-adding method similar to 119's method
    def minimumTotal2(self, triangle):
        nRows = len(triangle)
        helper = [0]*nRows  # cache array
        for i in range(nRows):
            for j in range(i, -1, -1):
                if j == 0:  # no left above, choose the above
                    helper[j] += triangle[i][0]
                elif j == i:    # no above, choose the left above
                    helper[j] = helper[j-1] + triangle[i][j]
                else:   # choose the smaller one from left above and above, then add to triangle[i][j]
                    helper[j] = min(helper[j], helper[j-1]) + triangle[i][j]
        return min(helper)

obj = Solution()
test_case = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
print(obj.minimumTotal2(test_case))