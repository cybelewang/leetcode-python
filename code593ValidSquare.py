"""
593 Valid Square


Given the coordinates of four points in 2D space, return whether the four points could construct a square.

The coordinate (x,y) of a point is represented by an integer array with two integers.

Example:
Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
Output: True
Note:

All the input integers are in the range [-10000, 10000].
A valid square has four equal sides with positive length and four equal angles (90-degree angles).
Input points have no order.
"""
class Solution:
    # reference http://www.cnblogs.com/grandyang/p/6914746.html
    # calculate all distances between two, and put the distances into a set
    # when the set has two non-zero distance, it's square
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        d = {self.distance2(p1, p2), self.distance2(p1, p3), self.distance2(p1, p4), self.distance2(p2, p3), self.distance2(p2, p4), self.distance2(p3, p4)}
        return 0 not in d and len(d) == 2
        
    # my own solution, check four distances, and then two diagonal distance, then the angle of the two diagonal lines
    def validSquare2(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        # sort input so p1 on the most left, and p4 on the most right
        p1, p2, p3, p4 = sorted([p1, p2, p3, p4])
        # check if four distances are equal
        d12 = self.distance2(p1, p2)
        d24 = self.distance2(p2, p4)
        d34 = self.distance2(p3, p4)
        d13 = self.distance2(p1, p3)

        # bug fixed: check diagnoal distance
        d23 = self.distance2(p2, p3)
        d14 = self.distance2(p1, p4)

        if d12*d24*d34*d13 == 0 or d23*d14== 0:
            return False

        if d12 != d24 or d24 != d34 or d34 != d13 or d12 != d13:
            return False

        # check if 14 and 23 are orthogonal
        return self.dotProduct((p4[0]-p1[0], p4[1] - p1[1]), (p3[0]-p2[0], p3[1]-p2[1])) == 0        


    def dotProduct(self, v1, v2):
        """
        return the dot product of two vectors: v1, v2
        """
        return v1[0]*v2[0] + v1[1]*v2[1]

    def crossProduct(self, v1, v2):
        """
        return the cross product's magnitude of two vectors: v1, v2
        """
        return v1[0]*v2[1] - v1[1]*v2[0]

    def distance2(self, v1, v2):
        """
        return the square of distance between two vector points
        """
        return (v2[0]-v1[0])**2 + (v2[1]-v1[1])**2

input = [[1,1], [5,3], [3,5], [7,7]] # expected False
print(Solution().validSquare(*input))