"""
223 Rectangle Area

Find the total area covered by two rectilinear rectangles in a 2D plane.

Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.

Rectangle Area
Assume that the total area is never beyond the maximum possible value of int.
"""
# rect1 + rect2 - overlap
# Note the tricky to figure out the overlap coordinates
# Can we assume the input integers are valid (they can form rectangles?)
class Solution:
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        # handle invalid rectangle parameters
        if C < A or D < B or G < E or H < F:
            return 0
        
        def area(A, B, C, D):
            if C < A or D < B:
                return 0
            else:
                return (C-A)*(D-B)

        return area(A, B, C, D) + area(E, F, G, H) - area(max(A, E), max(B, F), min(C, G), min(D, H))

obj = Solution()

print(obj.computeArea(-3, 0, 3, 4, 0, -1, 9, 2))