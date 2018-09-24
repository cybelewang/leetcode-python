"""
391 Perfect Rectangle

Given N axis-aligned rectangles where N > 0, determine if they all together form an exact cover of a rectangular region.
Each rectangle is represented as a bottom-left point and a top-right point. For example, a unit square is represented as [1,1,2,2]. (coordinate of bottom-left point is (1, 1) and top-right point is (2, 2)).

Example 1:
rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [3,2,4,4],
  [1,3,2,4],
  [2,3,3,4]
]
Return true. All 5 rectangles together form an exact cover of a rectangular region.

Example 2:
rectangles = [
  [1,1,2,3],
  [1,3,2,4],
  [3,1,4,2],
  [3,2,4,4]
]
Return false. Because there is a gap between the two rectangular regions.

Example 3:
rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [1,3,2,4],
  [3,2,4,4]
]
Return false. Because there is a gap in the top center.

Example 4:
rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [1,3,2,4],
  [2,2,4,4]
]
Return false. Because two of the rectangles overlap with each other.
"""
class Solution:
    # OJ's best solution
    def isRectangleCover(self, rectangles):
        area, corners = 0, set()
        a, c = lambda: (X - x) * (Y - y), lambda:{(x, y), (x, Y), (X, y), (X, Y)}
        for x, y, X, Y in rectangles:
            area += a()
            corners ^= c()
        x, y, X, Y = (f(z) for f,z in zip((min, min, max, max), zip(*rectangles)))
        return area == a() and corners == c()
    # Solution 2 from http://www.cnblogs.com/grandyang/p/5825619.html
    def isRectangleCover2(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        min_x, min_y, max_x, max_y = 2**31-1, 2**31-1, -2**31, -2**31
        exist, area = set(), 0
        for rect in rectangles:
            # update the outline rectange's coordinates
            min_x = min(min_x, rect[0])
            min_y = min(min_y, rect[1])
            max_x = max(max_x, rect[2])
            max_y = max(max_y, rect[3])

            # sum of all rect areas
            area += (rect[2]-rect[0])*(rect[3]-rect[1])

            # check if the 4 corners of this rect exist in set

            # bottom left
            if (rect[0], rect[1]) in exist:
                exist.remove((rect[0], rect[1]))
            else:
                exist.add((rect[0], rect[1]))

            # left top
            if (rect[0], rect[3]) in exist:
                exist.remove((rect[0], rect[3]))
            else:
                exist.add((rect[0], rect[3]))

            # right top
            if (rect[2], rect[3]) in exist:
                exist.remove((rect[2], rect[3]))
            else:
                exist.add((rect[2], rect[3]))

            # right bottom
            if (rect[2], rect[1]) in exist:
                exist.remove((rect[2], rect[1]))
            else:
                exist.add((rect[2], rect[1]))

        if (min_x, min_y) not in exist or \
            (min_x, max_y) not in exist or \
            (max_x, max_y) not in exist or \
            (max_x, min_y) not in exist or \
            len(exist) != 4:
            return False

        return area == (max_x-min_x)*(max_y-min_y)

obj = Solution()
rectangles = [[1,1,3,3], [3,1,4,2], [3,2,4,4], [1,3,2,4], [2,3,3,4]]
print(obj.isRectangleCover(rectangles))