"""
738 Monotone Increasing Digits

Given a non-negative integer N, find the largest number that is less than or equal to N with monotone increasing digits.

(Recall that an integer has monotone increasing digits if and only if each pair of adjacent digits x and y satisfy x <= y.)

Example 1:
Input: N = 10
Output: 9
Example 2:
Input: N = 1234
Output: 1234
Example 3:
Input: N = 332
Output: 299
Note: N is an integer in the range [0, 10^9].

"""
# similar problems: 31 Next Permutation
from functools import reduce
class Solution:
    # my own solution by finding the first peak digit
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N < 10:
            return N

        a = list(map(int, str(N)))  # get a list of digits of N
        pre, index = a[0], 0    # previous value and corresponding first index. For example, 1222233, when pre is 2, index is 1; when pre is 3, index is 5
        i = 1   # iterator
        while i < len(a):
            if a[i] > pre:  # update pre and index
                pre, index = a[i], i
            elif a[i] < pre:    # we find first digit that is smaller than previous digit, break here
                break
            i += 1

        if i == len(a): # N is monotone, just return it
            return N

        a[index] -= 1   # decrease most left of pre by 1
        for i in range(index+1, len(a)):    # assign the remaining right digits to 9
            a[i] = 9                

        return reduce(lambda x, y: x*10 + y, a)

    # http://www.cnblogs.com/grandyang/p/8068326.html
    def monotoneIncreasingDigits2(self, N):
        a = list(map(int, str(N)))
        n, j = len(a), len(a)
        for i in range(n-1, 0, -1):
            if a[i] >= a[i-1]:
                continue
            a[i-1] -= 1
            j = i
        
        for i in range(j, n):
            a[i] = 9

        return reduce(lambda x, y: x*10 + y, a)

test_N = [0, 8, 10, 1111, 1234, 232, 332, 2332, 545, 54345]
obj = Solution()
for N in test_N:
    print(N, end = ' -> ')
    print(obj.monotoneIncreasingDigits2(N))