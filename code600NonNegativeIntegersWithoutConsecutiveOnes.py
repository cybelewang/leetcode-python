"""
Given a positive integer n, find the number of non-negative integers less than or equal to n, whose binary representations do NOT contain consecutive ones.

Example 1:
Input: 5
Output: 5
Explanation: 
Here are the non-negative integers <= 5 with their corresponding binary representations:
0 : 0
1 : 1
2 : 10
3 : 11
4 : 100
5 : 101
Among them, only integer 3 disobeys the rule (two consecutive ones) and the other 5 satisfy the rule. 
Note: 1 <= n <= 10^9
"""
# similar problems: 474 Ones and Zeros
class Solution:
    # help from http://www.cnblogs.com/grandyang/p/6959585.html
    def findIntegers(self, num):
        """
        :type num: int
        :rtype: int
        """
        t = bin(num)[2:]    # binary form of num
        n = len(t)          # length of binary form

        # count number of distinct binary strings of length n without consecutive 1's
        # https://www.geeksforgeeks.org/count-number-binary-strings-without-consecutive-1s/
        zero, one = [0]*n, [0]*n    # zero[i] and one[i] are number of unique binary forms with length (i+1), ending with zero and one separately
        zero[0], one[0] = 1, 1
        for i in range(1, n):
            zero[i] = zero[i-1] + one[i-1]  # 0 can be appended to either o or 1
            one[i] = zero[i-1]  # 1 can only be appended to 0 to avoid consecutive 1's

        res = zero[-1] + one[-1]

        # now we need to remove those larger than num
        for i in range(1, n):
            if t[i] == '1' and t[i-1] == '1':   # if two consecutive 1's are seen, we can neglect the rest because they won't be larger than t
                break
            if t[i] == '0' and t[i-1] == '0':   # if two consecutive 0's are seen, we need to roll out the numbers with t[i] = 1
                res -= one[n-1-i]

        return res

    # solution 2 from http://www.cnblogs.com/grandyang/p/6959585.html
    def findIntegers2(self, num):
        """
        :type num: int
        :rtype: int
        """
        res, k, pre = 0, 31, 0
        f = [0]*32
        f[0], f[1] = 1, 2   # fibonacci series
        for i in range(2, 31):
            f[i] = f[i-1] + f[i-2]
        
        while k > -1:
            if num & (1 << k):
                res += f[k]
                if pre:
                    return res
                pre = 1
            else:
                pre = 0

            k -= 1
        
        return res + 1


obj = Solution()
for test in range(1, 100):
    r1 = obj.findIntegers(test)
    r2 = obj.findIntegers2(test)
    assert(r1==r2)