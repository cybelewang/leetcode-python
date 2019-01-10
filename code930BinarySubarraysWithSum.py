"""
930 Binary Subarrays With Sum

In an array A of 0s and 1s, how many non-empty subarrays have sum S?

Example 1:

Input: A = [1,0,1,0,1], S = 2
Output: 4
Explanation: 
The 4 subarrays are bolded below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]

Note:

A.length <= 30000
0 <= S <= A.length
A[i] is either 0 or 1.
"""
class Solution:
    def numSubarraysWithSum(self, A, S):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        """
        ones = [i for i, a in enumerate(A) if a == 1]   # indices in A where the value is 1
        N, ans = len(ones), 0
        # S == 0
        if S == 0:
            left = -1
            for i in range(N):
                if ones[i] > left + 1:
                    ans += 1
                left = ones[i]
            if N > left + 1:
                ans += 1
            return ans

        # S > 0
        for i in range(N-S+1):
            if i == 0:
                left = ones[i] + 1
            else:
                left = ones[i] - ones[i-1]
            
            j = i + S
            if j == N:
                right = len(A) - ones[j-1]
            else:
                right = ones[j] - ones[j-1]

            ans += left * right

        return ans

#A, S = [1,0,1,0,1], 1
A, S = [0, 0, 0, 0], 0
print(Solution().numSubarraysWithSum(A, S))