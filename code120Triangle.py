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

obj = Solution()
test_case = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
print(obj.minimumTotal(test_case))