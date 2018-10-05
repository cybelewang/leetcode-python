"""
788 Rotated Digits

X is a good number if after rotating each digit individually by 180 degrees, we get a valid number that is different from X.  Each digit must be rotated - we cannot choose to leave it alone.

A number is valid if each digit remains a digit after rotation. 0, 1, and 8 rotate to themselves; 2 and 5 rotate to each other; 6 and 9 rotate to each other, and the rest of the numbers do not rotate to any other number and become invalid.

Now given a positive number N, how many numbers X from 1 to N are good?

Example:
Input: 10
Output: 4
Explanation: 
There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.
Note:

N  will be in range [1, 10000].
"""
# if any digit is 2, 5, 6, 9, it will be a good number
# if any digit is 3, 4, 7, it won't be a good number
class Solution:
    # didn't consider that 3, 4, 7 won't form good numbers
    def rotatedDigits_WRONG(self, N):
        """
        :type N: int
        :rtype: int
        """
        f = [0]*5   # f[i] is the count of good numbers from length-0 to length-i numbers
        f[1] = 4    # single digit good numbers are only 2, 5, 6, 9
        for i in range(2, 5):
            f[i] = 6*f[i-1]   # when the highest digit is 0, 1, 3, 4, 7, 8
            f[i] += 4*(10**(i-1))   # when the highest digit is 2, 5, 6, 9, numbers are always good no matter the rest of the digits

        def helper(N, f):
            if N < 1:
                return 0

            highest = int(str(N)[0])    # highest digit
            n = len(str(N)) # number of digits
            res = 0
            # calculate the previous highest digits' result, for example, N = 2345, we will figure out the result for 0XXX, and 1XXX
            for d in range(highest-1, -1, -1):
                if d in (2, 5, 6, 9):
                    res += 10**(n-1)
                else:
                    res += f[n-1]
            # now calculate the number with highest digit, with example N = 2345, this will calculate the result for 2XXX
            if highest in (2, 5, 6, 9):
                res += 1 + N % (10**(n-1))
            else:
                res += helper(N % (10**(n-1)), f)

            return res

        # main
        return helper(N, f)
    
    # brutal force solution
    def rotatedDigits(self, N):
        res = 0
        good = set(['2', '5', '6', '9'])
        bad = set(['3', '4', '7'])
        for num in range(1, N+1):
            s = str(num)
            if any(c in bad for c in s):
                continue
            if any(c in good for c in s):
                res += 1

        return res

    # DP solution http://www.cnblogs.com/grandyang/p/9154892.html
 #   def rotatedDigits_DP(self, N):

N = 857 # expected 247
print(Solution().rotatedDigits(N))
