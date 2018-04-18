"""
You are given two jugs with capacities x and y litres. There is an infinite amount of water supply available. You need to determine whether it is possible to measure exactly z litres using these two jugs.

If z liters of water is measurable, you must have z liters of water contained within one or both buckets by the end.

Operations allowed:

Fill any of the jugs completely with water.
Empty any of the jugs.
Pour water from one jug into another till the other jug is completely full or the first jug itself is empty.
Example 1: (From the famous "Die Hard" example)

Input: x = 3, y = 5, z = 4
Output: True
Example 2:

Input: x = 2, y = 6, z = 5
Output: False
"""
# http://www.cnblogs.com/grandyang/p/5628836.html
# https://en.wikipedia.org/wiki/B%C3%A9zout%27s_identity
class Solution:
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        def gcd(x, y):
            """
            get greatest common divisor of x and y
            famous Euclidean algorithm
            """
            return x if y == 0 else gcd(y, x % y)

        return z == 0 or ((x + y >= z) and (z % gcd(x, y) == 0))

print(Solution().canMeasureWater(3, 5, 4))