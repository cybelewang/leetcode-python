"""
For an integer n, we call k>=2 a good base of n, if all digits of n base k are 1.

Now given a string representing n, you should return the smallest good base of n in string format. 

Example 1:
Input: "13"
Output: "3"
Explanation: 13 base 3 is 111.
Example 2:
Input: "4681"
Output: "8"
Explanation: 4681 base 8 is 11111.
Example 3:
Input: "1000000000000000000"
Output: "999999999999999999"
Explanation: 1000000000000000000 base 999999999999999999 is 11.
Note:
The range of n is [3, 10^18].
The string representing n is always valid and will not have leading zeros.
"""
from math import log
class Solution:
    # improved solution from http://www.cnblogs.com/grandyang/p/6620351.html
    def smallestGoodBase(self, n):
        """
        :type n: str
        :rtype: str
        """
        N = int(n)
        M = int(log(N, 2)) + 1
        for m in range(M, 1, -1):
            lo = int((N+1)**(1.0/m)) - 1
            hi = int(N**(1.0/(m-1))) + 1
            while lo <= hi:
                mid = (lo + hi)//2
                num = 0
                for _ in range(m):
                    num = num*mid + 1
                if num == N:
                    return str(mid)
                elif num > N:
                    hi = mid - 1
                else:
                    lo = mid + 1
            
        return str(N-1)

print(Solution().smallestGoodBase('1000000000000000000'))
                