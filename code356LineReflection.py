"""
356 Line Reflection

Given n points on a 2D plane, find if there is such a line parallel to y-axis that reflect the given set of points.

Example 1:
Given points = [[1,1],[-1,1]], return true.

Example 2:
Given points = [[1,1],[-1,-1]], return false.

Follow up:
Could you do better than O(n2)?

Hint:

Find the smallest and largest x-value for all points.
If there is a line then it should be at y = (minX + maxX) / 2.
For each point, make sure that it has a reflected point in the opposite side.
"""
import unittest
class Solution:
    def isReflected(self, points):
        if not points:
            return False
        points.sort(key = lambda p: (p[1], p[0]))

        start = 0
        center = set()
        for i in range(len(points)):
            if i + 1 < len(points) and points[i][1] == points[i+1][1]:
                continue
            end = i
            while start <= end:
                center.add(points[start][0] + points[end][0])
                if len(center) > 1:
                    return False
                start += 1
                end -= 1
            start = i + 1
        
        return True

obj = Solution()
class Test(unittest.TestCase):
    def test_1(self):
        self.assertTrue(obj.isReflected([[1, 1],[-1, 1]]))
        self.assertFalse(obj.isReflected([[1, 1],[-1, -1]]))

if __name__ == "__main__":
    unittest.main(exit=False)