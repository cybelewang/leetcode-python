"""
402 Remove K Digits

Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.

Note:
The length of num is less than 10002 and will be ≥ k.
The given num does not contain any leading zero.
Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.
"""
# use a deque
# if this digit d < last digit in deque, keep poping the last digit from deque until d >= last digit, or deque is empty, or count == k
# if count still < k after the above process, removing large digits from the end to beginning (pop method)
# remove leading '0's
# finally if stack is empty return '0' otherwise return the actual stack string
from collections import deque
class Solution:
    # OJ's best solution
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        out, n = [], len(num) - k # n is the final result's length
        for digit in num:
            while k and out and out[-1] > digit:
                out.pop()
                k-=1
            out.append(digit)
        #print(out)
        return ''.join(out[:n]).lstrip('0') or "0"
        
    # my own solution
    def removeKdigits2(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = deque()
        count = 0
        for d in num:
            while count < k and stack and d < stack[-1]:
                stack.pop()
                count += 1

            stack.append(d)

        # remove large digits from end
        while stack and count < k:
            stack.pop()
            count += 1
        
        # remove leading '0's
        while stack and stack[0] == '0':
            stack.popleft()
        
        return ''.join(stack) if stack else '0'

    def removeKdigits_DFS(self, num, k):
        def helper(s, k):
            res = ''
            if len(s) <= k: return ''
            i, minVal = 0, '99' # change minVal to '' for follow-up
            for j in range(k+1):
                if s[j] < minVal: # we can't use <= because this will remove too many small digits, example num = 112, k = 2
                    i = j
                    minVal = s[j]
            if i == k:
                res = s[i:]
            else:
                res = s[i] + helper(s[i+1:], k-i)

            return res

        if k >= len(num):
            return '0'
        return helper(num, k).lstrip('0') or '0'


test_cases = [('1', 1), ('78912', 3), ('1432219', 3), ('100200', 1), ('100',1)]
obj = Solution()
for num, k in test_cases:
    print(obj.removeKdigits(num, k))