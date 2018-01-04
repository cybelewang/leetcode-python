"""
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
"""
# Ask if n is not positive?
from collections import deque
class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        base = ord('A')
        letters = deque()
        while n > 0:
            letters.appendleft(chr((n-1)%26 + base))
            n = (n-1)//26
        
        return ''.join(letters)

obj = Solution()
for n in [1, 26, 27, 52, 53, 676, 677, 702, 703]:
    print(n, end=' -> ')
    print(obj.convertToTitle(n))