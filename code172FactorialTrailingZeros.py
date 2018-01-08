"""
Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.
"""
# Each '5' in the i <= n contributes to a '0'
class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        return 0 if n == 0 else n//5 + self.trailingZeroes(n//5) 

    # TLE    
    def trailingZeroes2(self, n):
        """
        :type n: int
        :rtype: int
        """
        def count5s(n):
            """
            count how many 5 in n            
            """
            count = 0
            while n > 0 and n % 5 == 0:
                count += 1
                n //= 5
            
            return count
        
        res = 0
        for i in range(1, n+1):
            res += count5s(i)

        return res

obj = Solution()
test_cases = [0, 5, 10, 100, 1000, 10000, 100000]
for case in test_cases:
    print(obj.trailingZeroes(case))   