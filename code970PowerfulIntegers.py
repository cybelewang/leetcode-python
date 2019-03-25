"""
970 Powerful Integers

Given two positive integers x and y, an integer is powerful if it is equal to x^i + y^j for some integers i >= 0 and j >= 0.

Return a list of all powerful integers that have value less than or equal to bound.

You may return the answer in any order.  In your answer, each value should occur at most once.

Example 1:

Input: x = 2, y = 3, bound = 10
Output: [2,3,4,5,7,9,10]
Explanation: 
2 = 2^0 + 3^0
3 = 2^1 + 3^0
4 = 2^0 + 3^1
5 = 2^1 + 3^1
7 = 2^2 + 3^1
9 = 2^3 + 3^0
10 = 2^0 + 3^2
Example 2:

Input: x = 3, y = 5, bound = 15
Output: [2,4,6,8,10,14]

Note:

1 <= x <= 100
1 <= y <= 100
0 <= bound <= 10^6
"""
class Solution:
    def powerfulIntegers(self, x, y, bound):
        """
        :type x, y, bound: int
        :rtype: list[int]
        """
        xs, ys = [1], [1]
        while xs[-1] < x*xs[-1] <= bound:
            xs.append(x*xs[-1])
        
        while ys[-1] < y*ys[-1] <= bound:
            ys.append(y*ys[-1])

        unique = set()
        for a in xs:
            if a > bound:
                break
            for b in ys:
                if a + b > bound:
                    break
                unique.add(a + b)

        return list(unique) 

print(Solution().powerfulIntegers(3, 5, 15))
