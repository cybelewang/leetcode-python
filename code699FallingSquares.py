"""
On an infinite number line (x-axis), we drop given squares in the order they are given.

The i-th square dropped (positions[i] = (left, side_length)) is a square with the left-most point being positions[i][0] and sidelength positions[i][1].

The square is dropped with the bottom edge parallel to the number line, and from a higher height than all currently landed squares. We wait for each square to stick before dropping the next.

The squares are infinitely sticky on their bottom edge, and will remain fixed to any positive length surface they touch (either the number line or another square). Squares dropped adjacent to each other will not stick together prematurely.


Return a list ans of heights. Each height ans[i] represents the current highest height of any square we have dropped, after dropping squares represented by positions[0], positions[1], ..., positions[i].

Example 1:
Input: [[1, 2], [2, 3], [6, 1]]
Output: [2, 5, 5]
Explanation:

After the first drop of positions[0] = [1, 2]:
_aa
_aa
-------
The maximum height of any square is 2.


After the second drop of positions[1] = [2, 3]:
__aaa
__aaa
__aaa
_aa__
_aa__
--------------
The maximum height of any square is 5.  
The larger square stays on top of the smaller square despite where its center
of gravity is, because squares are infinitely sticky on their bottom edge.


After the third drop of positions[1] = [6, 1]:
__aaa
__aaa
__aaa
_aa
_aa___a
--------------
The maximum height of any square is still 5.

Thus, we return an answer of [2, 5, 5].


Example 2:
Input: [[100, 100], [200, 100]]
Output: [100, 100]
Explanation: Adjacent squares don't get stuck prematurely - only their bottom edge can stick to surfaces.
Note:

1 <= positions.length <= 1000.
1 <= positions[i][0] <= 10^8.
1 <= positions[i][1] <= 10^6.
"""
# similar problems: 218 The Skyline Problem
class Solution:
    def fallingSquares_OJBest(self, positions):
        """
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        
        # heights[k]: current height for range [coords[k], coords[k+1])
        coords = [0, math.inf]
        heights = [0, 0]
        
        res = []
        for l, h in positions:
            r = l + h
            l_idx = bisect.bisect_right(coords, l)
            r_idx = bisect.bisect_left(coords, r)
            
            new_h = max(heights[l_idx-1:r_idx]) + h
            # print(l,r,l_idx,r_idx,coords, heights)
            coords[l_idx:r_idx] = [l, r]
            heights[l_idx:r_idx] = [new_h, heights[r_idx-1]]
            # print(l,r,l_idx,r_idx,coords, heights)
            res.append(max(res[-1] if res else 0, new_h))

        return res
    # brutal force solution from http://www.cnblogs.com/grandyang/p/8486414.html
    def fallingSquares(self, positions):
        """
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        n = len(positions)
        heights = [0]*n

        res, h = [], 0  # result and current max height 
        for i in range(n):
            left, length = positions[i]
            right = left + length
            heights[i] += length    # add height onto the base height[i]

            h = max(h, heights[i])
            res.append(h)

            for j in range(i+1, n):
                l, len_ = positions[j]
                r = l + len_
                if l < right and r > left:  # try to slide j on top of i and get these conditions
                    heights[j] = max(heights[j], heights[i])

        return res

positions = [[1, 2], [2, 3], [6, 1]]
print(Solution().fallingSquares(positions))