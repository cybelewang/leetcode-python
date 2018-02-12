"""
Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.

For example:
Given n = 13,
Return 6, because digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.
"""
# divide the number to a few ranges, for example, 23456 can be 0-9999, 10000-19999, 20000-23456
# We can pre-calculate 0-9999 as value full_range_ones[4], so 0-19999 will be 2*full_range_ones[4]. 
# Now consider the starting "1" in 10000-19999, it is 10**4. Becareful to numbers like 12345 because it will not reach range 19999.
# The remaining 20000-23456 will be the same as 3456 and we can recursively figure out the value.
class Solution:
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        full_range_ones = [0]  # index is the length of full numbers like 999, and value is the number of digit one in the range of 0 to full number like 999
        for i in range(1, 11):
            num = 10 * full_range_ones[-1] + 10**(i-1) # how to get value of 0-999 from 0-99? We add one digit 0-9, which means 10 times of previous value, add 0-99 times of starting "1"
            full_range_ones.append(num)
        
        #print(full_range_ones)
        # full_range_ones = [0, 1, 20, 300, 4000, 50000, 600000, 7000000, 80000000, 900000000, 10000000000]
        # This means from 0-9 there is 1 digit One, and 0-99 there are 20 digit Ones, and 0-999 there are 300 digit Ones...

        def _dfs(n, full_range_ones):
            k, m = 0, n # k is length of n
            while m > 0:
                m = m//10
                k += 1

            if n == 0:
                return 0
            else:
                highest, remain = divmod(n, 10**(k-1))
 
                res = highest*full_range_ones[k-1]
                res += remain + 1 if highest == 1 else 10**(k-1) 
                res += _dfs(remain, full_range_ones)

                return res


        return _dfs(n, full_range_ones)

obj = Solution()
print(obj.countDigitOne(13))