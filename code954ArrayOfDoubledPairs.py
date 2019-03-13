"""
954 Array of Doubled Pairs

Given an array of integers A with even length, return true if and only if it is possible to reorder it such that A[2 * i + 1] = 2 * A[2 * i] for every 0 <= i < len(A) / 2.

Example 1:

Input: [3,1,3,6]
Output: false
Example 2:

Input: [2,1,2,6]
Output: false
Example 3:

Input: [4,-2,2,-4]
Output: true
Explanation: We can take two groups, [-2,-4] and [2,4] to form [-2,-4,2,4] or [2,4,-2,-4].
Example 4:

Input: [1,2,4,16,8,4]
Output: false

Note:

0 <= A.length <= 30000
A.length is even
-100000 <= A[i] <= 100000
"""
from collections import Counter
class Solution:
    def canReorderDoubled(self, A):
        count = Counter(A)
        for a in sorted(A, key = abs):
            if count[a] == 0:
                continue
            if count[2*a] == 0:
                return False

            count[a] -= 1
            count[2*a] -= 1
        
        return True
            
    # wrong solution, cannot pass A = [-1,4,6,8,-4,6,-6,3,-2,3,-3,-8], expect true
    def canReorderDoubled_WRONG(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        count = defaultdict(int)
        for a in A:
            if count[a*2] > 0:
                count[a*2] -= 1
            elif a%2 == 0 and count[a//2] > 0:
                count[a//2] -= 1
            else:
                count[a] += 1
        print(count)
        return all(count[key] == 0 for key in count)

#A = [2,1,2,1,1,1,2,2]   # expect true
A = [-1,4,6,8,-4,6,-6,3,-2,3,-3,-8] # expect true
print(Solution().canReorderDoubled(A))
