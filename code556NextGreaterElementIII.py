"""
556 Next Greater Element III


Given a positive 32-bit integer n, you need to find the smallest 32-bit integer which has exactly the same digits existing in the integer n and is greater in value than n. 
If no such positive 32-bit integer exists, you need to return -1.

Example 1:

Input: 12
Output: 21
 

Example 2:

Input: 21
Output: -1
"""
# similar problems: 31 next permutation
class Solution:
    # my own solution
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        # convert integer to a list of digits
        d = list(str(n))
        m = len(d)
        if m < 2:
            return -1

        # search from right to left, for the first position i where d[i] > d[i-1]
        i = m - 1
        while i > 0 and d[i] <= d [i-1]:
            i -= 1
        
        # d is in reversed order, no next greater integer
        if i == 0:
            return -1

        # now d[i] > d[i-1], we need to find d[j] to replace d[i-1], d[j] must be the smallest digit > d[i-1], so we must search d[i:] to find d[j]
        j = i
        while j < m-1 and d[j+1] > d[i-1]:
            j += 1

        # now switch [i-1] and [j]
        d[i-1], d[j] = d[j], d[i-1]

        # then sort d[i:]
        a = sorted(d[i:])
        d[i:] = a

        res = int(''.join(d))        

        return -1 if res > 2**31 - 1 else res   # bug fixed: the problem states that for result > 2**31-1, return -1

test_cases = [0, 12, 21, 100, 101, 1234, 1243, 1342, 43211, 12334, 12433, 1999999999]
obj = Solution()
for n in test_cases:
    print(n, end = ' -> ')
    print(obj.nextGreaterElement(n))