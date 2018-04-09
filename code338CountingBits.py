"""
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num 
calculate the number of 1's in their binary representation and return them as an array.

Example:
For num = 5 you should return [0,1,1,2,1,2].

Follow up:

It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.
"""
class Solution:
    # By observation, we find that (1) if number is power of 2, the result is 1
    # (2) res[i] = 1 + res[i-power], where power is the closest power of 2 and <= current number
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = [0]*(num+1)
        power = 1
        for i in range(1, num+1):
            if (i & (i - 1)) == 0:  # check if this number i is power of 2 by turning off the most right bit 1
                res[i] = 1
                power = i
            else:
                res[i] = 1 + res[i - power]

        return res

obj = Solution()
print(obj.countBits(17))