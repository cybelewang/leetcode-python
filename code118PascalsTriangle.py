"""
118 Pascal's Triangle

Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = [[1], [1, 1]]

        if numRows < 3:
            return res[:numRows]

        for n in range(3, numRows + 1):
            row = [1]
            for j in range(0, len(res[-1]) - 1):
                row.append(res[-1][j] + res[-1][j+1])
            row.append(1)
            res.append(row)
        
        return res

obj = Solution()
print(obj.generate(7))