"""
Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

Note:
n is positive and will fit within the range of a 32-bit signed integer (n < 2^31).

Example 1:

Input:
3

Output:
3
Example 2:

Input:
11

Output:
0

Explanation:
The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.
"""
class Solution:
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        length, count = 0, 0
        while count < n:
            length += 1
            count += 9*(10**(length-1))*length
            
        count -= 9*(10**(length-1))*length

        num = 10**(length - 1) + (n-count-1)//length
        return ord(str(num)[(n-count-1)%length]) - ord('0')

obj = Solution()
print(obj.findNthDigit(2**31-1))