"""
587 Erect the Fence


There are some trees, where each tree is represented by (x,y) coordinate in a two-dimensional garden. 
Your job is to fence the entire garden using the minimum length of rope as it is expensive. 
The garden is well fenced only if all the trees are enclosed. Your task is to help find the coordinates of trees which are exactly located on the fence perimeter.

Example 1:
Input: [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
Output: [[1,1],[2,0],[4,2],[3,3],[2,4]]
Explanation:

Example 2:
Input: [[1,2],[2,2],[4,2]]
Output: [[1,2],[2,2],[4,2]]
Explanation:

Even you only have trees in a line, you need to use rope to enclose them. 
Note:

All trees should be enclosed together. You cannot cut the rope to enclose trees that will separate them in more than one group.
All input integers will range from 0 to 100.
The garden has at least one tree.
All coordinates are distinct.
Input points have NO order. No order required for output.
"""

class Point:    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return '['+str(self.x)+','+str(self.y)+']'

from functools import reduce
class Solution:
    # help from https://www.cnblogs.com/weedboy/p/6896478.html
    def outerTrees(self, points):
        """
        :type points: List[Point]
        :rtype: List[Point]
        """
        def sign(p, q, r):
            # < 0: r is on the right side of vector p->q (or external)
            # == 0: r is on the line of vector p->q
            # > 0: r is on the left side of vector p->q (or inner)
            return (p.x-r.x)*(q.y-r.y) - (p.y-r.y)*(q.x-r.x)

        def drive(hull, r): # reduce inner call: accum_value = func(accum_value, p)
            hull.append(r)
            while len(hull) > 2 and sign(*hull[-3:]) < 0:
                hull.pop(-2)
            
            return hull

        # main
        points.sort(key = lambda p: (p.x, p.y))
        # get lower board
        lower = reduce(drive, points, [])
        # get upper board
        upper = reduce(drive, points[::-1], [])

        return list(set(lower + upper))


nums = [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
points = []
for x, y in nums:
    points.append(Point(x, y))

print(Solution().outerTrees(points))
        