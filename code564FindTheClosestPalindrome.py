"""
564 Find the Closest Palindrome

Given an integer n, find the closest integer (not including itself), which is a palindrome.

The 'closest' is defined as absolute difference minimized between two integers.

Example 1:
Input: "123"
Output: "121"
Note:
The input n is a positive integer represented by string, whose length will not exceed 18.
If there is a tie, return the smaller one as answer.
"""
class Solution:
    # help from http://www.cnblogs.com/grandyang/p/6915355.html
    # 1. use a set to temporarily hold all candidate results
    # 2. for any number n with a length of len, the result must be within a range of [10^(len-1) - 1, 10^len + 1]. For example, for 3-digit number, the range is [99, 1001]
    # 3. take the left half of n (for odd-length n, include the middle digit) and get prefix
    # 4. add -1, 0, 1 to prefix's last digit, and get a new integer pre
    # 5. for each pre, reverse pre and append it to the end of pre (for odd-length n, we exclude the middle digit), and get a candidate
    # 6. remove original number n from candidate set (problem requirement)
    # 7. iterate all numbers in the set and find the one with minimum absolute difference with n
    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """
        digits, num = list(n), int(n)
        length = len(digits)

        candidates = set()  # all possible results will be put in this set
        candidates.add(10**length + 1)
        candidates.add(10**(length-1) - 1)  # the result is within a range of [10^(len-1) - 1, 10^len + 1]. For example, for 3-digit number, the range is [99, 1001]

        prefix = int(n[:(length+1)//2])  # for odd-length number n, include the middle digit, for even-length number, just the left half

        for i in range(-1,2):   # add -1, 0, 1 seperately for prefix's last digit
            pre = str(prefix + i)
            m = len(pre)
            s = pre + pre[0:m-(length&1)][::-1] # if length is odd, then length & 1 is 1 and we exclude the last digit of pre
            candidates.add(int(s))

        if num in candidates:
            candidates.remove(num)    # if n is palindrome, then remove it because problem requires this

        # iterate the candidates set and find the one with minimum absolute difference
        min_diff = 2**63 - 1
        res = min_diff
        for i in candidates:
            diff = abs(i - num)
            if diff < min_diff:
                min_diff = diff
                res = i
            elif diff == min_diff:
                res = min(res, i)

        return str(res)

test_cases = ['1', '11', '100', '111', '1111', '123']
if __name__ == '__main__':
    for n in test_cases:
        print(n, end = ' -> ')
        print(Solution().nearestPalindromic(n))