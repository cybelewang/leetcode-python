"""
735 Asteroid Collision

We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

Example 1:
Input: 
asteroids = [5, 10, -5]
Output: [5, 10]
Explanation: 
The 10 and -5 collide resulting in 10.  The 5 and 10 never collide.
Example 2:
Input: 
asteroids = [8, -8]
Output: []
Explanation: 
The 8 and -8 collide exploding each other.
Example 3:
Input: 
asteroids = [10, 2, -5]
Output: [10]
Explanation: 
The 2 and -5 collide resulting in -5.  The 10 and -5 collide resulting in 10.
Example 4:
Input: 
asteroids = [-2, -1, 1, 2]
Output: [-2, -1, 1, 2]
Explanation: 
The -2 and -1 are moving left, while the 1 and 2 are moving right.
Asteroids moving the same direction never meet, so no asteroids will meet each other.
Note:

The length of asteroids will be at most 10000.
Each asteroid will be a non-zero integer in the range [-1000, 1000]..
"""
# similar problems: 605 Can Place Flowers
class Solution:
    # solution 2 from http://www.cnblogs.com/grandyang/p/8035551.html
    # we use a list "res" to save the result, and iterate all elements in asteroids
    # the "front line" is the end of "res"
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        res, i = [], 0
        while i < len(asteroids):
            if asteroids[i] > 0:
                res.append(asteroids[i])
            elif not res or res[-1] < 0:
                res.append(asteroids[i])
            elif res[-1] <= -asteroids[i]:
                if res[-1] < -asteroids[i]:
                    i -= 1
                res.pop()
            
            i += 1

        return res

    # my own solution, TLE
    # divide asteroids into two same-size list: pos and neg. 
    # pos holds the positive asteroid, or 0 if that position is negative
    # neg holds the negative asteroid, or 0 if that position is positive
    # everytime we overlap pos[:sub] and neg[N-sub:], add them element-wise using the rule as describe above
    # finally we assemble the result by collecting non-zero values left in neg and pos
    def asteroidCollision2(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        pos, neg = [], []    # asteroids to right, asteroids to left, 0 means that position's asteroid is either empty or moving to opposite direction
        for num in asteroids:
            if num > 0:
                pos.append(num)
                neg.append(0)
            else:
                neg.append(num)
                pos.append(0)
        
        N = len(asteroids)
        for overlap in range(N-1, 0, -1):
            for i in range(overlap):
                j = N - overlap + i
                if pos[i] + neg[j] > 0:
                    neg[j] = 0
                elif pos[i] + neg[j] < 0:
                    pos[i] = 0
                else:
                    pos[i], neg[j] = 0, 0
        
        return [size for size in neg + pos if size != 0]

a = [1, -1, -1, 1, -1, 1]
print(Solution().asteroidCollision(a))