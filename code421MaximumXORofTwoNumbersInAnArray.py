"""
421 Maximum XOR of Two Numbers in an Array

Given a non-empty array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai < 2**31.

Find the maximum result of ai XOR aj, where 0 ≤ i, j < n.

Could you do this in O(n) runtime?

Example:

Input: [3, 10, 5, 25, 2, 8]

3   00011
10  01010
5   00101
25  11001
2   00010
8   01000

Output: 28

Explanation: The maximum result is 5 ^ 25 = 28.
"""
class Solution:
    # Let's figure out how to get the high nth bit in result
    # for each number, keep only the highest n bits, set (32-n) lowest bits to 0, and put the result into a set
    # create a number tmp equal to result, then set the nth bit of tmp to be 1
    # try to find two pre-n-bit numbers in the set that their XOR result is tmp. 
    # This can be done through checking if tmp ^ pre in set, because if pre1 ^ pre2 = tmp, then pre1 ^ tmp = pre2. 
    # This is similar to "Two Sum", using space to exchange with time
    # If we cannot find the above two pre-n-bit numbers in the set, that means nth bit should be 0 in result
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # if a ^ b = x, then a ^ x = b, a = b ^ x
        # https://kingsfish.github.io/2017/12/15/Leetcode-421-Maximum-XOR-of-Two-Numbers-in-an-Array/
        res, mask = 0, 0
        for i in range(31, -1, -1):
            mask = mask | (1 << i)  # n = 32-i, all n high bits are '1', for example, if i=30, n=2, then mask = 1100000000000000000000...
            myset = set()
            for num in nums:
                myset.add(mask & num) # put the prefix n high bits of each number into myset
            
            tmp = res | (1 << i)    # assume nth bit in result is '1', this makes sure the result is the largest
            for pre in myset:
                # if a ^ b = x, then a ^ x = b, a = b ^ x
                if (tmp ^ pre) in myset: # check if two pres in mytest with their xor result equal to tmp. The two pres must not equal, otherwise their xor result will be 0.
                    res = tmp   # there are two pre in mytest and their XOR is tmp, so update res to tmp
                    break
            
        return res

nums = [3, 10, 5, 25, 2, 8]
print(Solution().findMaximumXOR(nums))