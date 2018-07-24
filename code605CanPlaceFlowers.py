"""
Suppose you have a long flowerbed in which some of the plots are planted and some are not. 
However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.

Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), and a number n, 
return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: True
Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: False
Note:
The input array won't violate no-adjacent-flowers rule.
The input array size is in the range of [1, 20000].
n is a non-negative integer which won't exceed the input array size.
"""
class Solution:
    # my own solution, find the number of 0's betweeen two 1's. virtually add [1, 0] at beginning, and [0, 1] at end
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        last, res = -2, 0   # initially virtually assume there is a '1' in index -2, a '0' in index -1
        # add 0 and 1 to the end because flower can be placed in the end if the left is 0
        flowerbed.append(0)
        flowerbed.append(1)

        for i, state in enumerate(flowerbed):
            if state:
                zeros = i - last - 1    # number of 0's between two 1's
                res += max(0, (zeros-1)//2) # use examples to find the rules, like 5 zeros result 2, 6 zeros result 2
                last = i
        
        print(res)
        return res >= n

f= [0, 0, 0, 0, 0, 0]
print(Solution().canPlaceFlowers(f, 1))