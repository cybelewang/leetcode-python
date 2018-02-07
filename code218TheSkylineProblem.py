"""
A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Now suppose you are given the locations and height of all the buildings as shown on a cityscape photo (Figure A), write a program to output the skyline formed by these buildings collectively (Figure B).

 Buildings  Skyline Contour
The geometric information of each building is represented by a triplet of integers [Li, Ri, Hi], where Li and Ri are the x coordinates of the left and right edge of the ith building, respectively, and Hi is its height. It is guaranteed that 0 ≤ Li, Ri ≤ INT_MAX, 0 < Hi ≤ INT_MAX, and Ri - Li > 0. You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.

For instance, the dimensions of all buildings in Figure A are recorded as: [ [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ] .

The output is a list of "key points" (red dots in Figure B) in the format of [ [x1,y1], [x2, y2], [x3, y3], ... ] that uniquely defines a skyline. A key point is the left endpoint of a horizontal line segment. Note that the last key point, where the rightmost building ends, is merely used to mark the termination of the skyline, and always has zero height. Also, the ground in between any two adjacent buildings should be considered part of the skyline contour.

For instance, the skyline in Figure B should be represented as:[ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ].

Notes:

The number of buildings in any input list is guaranteed to be in the range [0, 10000].
The input list is already sorted in ascending order by the left x position Li.
The output list must be sorted by the x position.
There must be no consecutive horizontal lines of equal height in the output skyline. For instance, [...[2 3], [4 5], [7 5], [11 5], [12 7]...] is not acceptable; the three lines of height 5 should be merged into one in the final output as such: [...[2 3], [4 5], [12 7], ...]
"""
from functools import cmp_to_key
class Solution:
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        encode = []   # [0]: Li, [1]: Ri, [2]: 1 for rising edge, 0 for failing edge
        for b in buildings:
            encode.append([b[0], b[2], 1])  # raising edge
            encode.append([b[1], b[2], 0])  # falling edge
        
        # compare function to sort the encode entries
        def _cmp(x, y):
            if x[0] == y[0]:
                if x[2] == y[2]:
                    return x[1] - y[1]
                else:
                    return x[2] - y[2]
            else:
                return x[0] - y[0]
            
        # sort the encode by x coordinates
        encode = list(sorted(encode, key = cmp_to_key(_cmp)))

        res, heap = [], [0]
        prev_h = 0
        for b in encode:
            if b[2] == 1:
                # rising edge
                x, h = b[0], b[1]
                heap.append(h)
                heap.sort()
                if h > prev_h:
                    res.append([x, h])
                    prev_h = h
            else:
                # falling edge
                heap.remove(b[1])
                heap.sort()
                h = heap[-1]
                if h < prev_h:
                    res.append([b[0], h])
                    prev_h = h

        # post-process res to remove the same x
        merge = []
        for item in res:
            if len(merge) > 0 and merge[-1][0] == item[0]:
                merge[-1][1] = max(merge[-1][1], item[1])
            else:
                merge.append(item[:])
        
        # remove entries with the same height
        res = []
        for item in merge:
            if len(res) > 0 and res[-1][1] == item[1]:
                pass
            else:
                res.append(item)

        return res

obj = Solution()
#test_case = [[1, 2, 10], [1, 3, 10], [3, 4, 10]]
test_case = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
print(obj.getSkyline(test_case))