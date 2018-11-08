"""
858 Mirror Reflection

There is a special square room with mirrors on each of the four walls.  Except for the southwest corner, there are receptors on each of the remaining corners, numbered 0, 1, and 2.

The square room has walls of length p, and a laser ray from the southwest corner first meets the east wall at a distance q from the 0th receptor.

Return the number of the receptor that the ray meets first.  (It is guaranteed that the ray will meet a receptor eventually.)

 

Example 1:

Input: p = 2, q = 1
Output: 2
Explanation: The ray meets receptor 2 the first time it gets reflected back to the left wall.



Note:

1 <= p <= 1000
0 <= q <= p
"""
"""
Instead of modelling the ray as a bouncing line, model it as a straight line through reflections of the room.

For example, if p = 2, q = 1, then we can reflect the room horizontally, and draw a straight line from (0, 0) to (4, 2). The ray meets the receptor 2, which was reflected from (0, 2) to (4, 2).

In general, the ray goes to the first integer point (kp, kq) where k is an integer, and kp and kq are multiples of p. Thus, the goal is just to find the smallest k for which kq is a multiple of p.

The mathematical answer is k = p / gcd(p, q).
"""

from fractions import gcd
class Solution:
    def mirrorReflection(self, p, q):
        """
        :type p: int
        :type q: int
        :rtype: int
        """
        g = gcd(p, q)
        p = (p // g) % 2
        q = (q // g) % 2

        return 1 if p and q else 0 if p else 2
        