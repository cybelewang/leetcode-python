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
    # my own solution by calculating the leading and trailing zeros of S 1s
    def numSubarraysWithSum(self, A, S):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        """
        ones = [i for i, a in enumerate(A) if a == 1]   # indices in A where the value is 1
        N, ans, pre = len(ones), 0, -1
        # S == 0, need to calculate number of subarrays with all 0s, and these subarrays exist between two 1s        
        if S == 0:
            pre = -1   # virtual 1 on index -1
            for i in range(N):
                ans += (ones[i]-pre-1)*(ones[i]-pre)//2   # if index i and j have 1s, then there are n = (j-i-1) zeros between them, and there are n*(n+1)//2 non-empty subarrays
                pre = ones[i]
            ans += (len(A)-pre-1)*(len(A)-pre)//2 # don't forget the trailing zeros

            return ans

        # S > 0, need to calculate the leading zeros and trailing zeros of the subarray
        for i in range(N-S+1):
            if i == 0:
                left = ones[i] + 1
            else:
                left = ones[i] -ones[i-1]   # # there are (ones[i]-ones[i-1]-1) zeros, but we have (ones[i]-ones[i-1]-1+1) = (ones[i]-ones[i-1]) selections, including the case of no zeros
            
            j = i + S   # trailing zeros are between j-1 and j
            if j == N:
                right = len(A) - ones[j-1]
            else:
                right = ones[j] - ones[j-1]

            ans += left * right

        return ans

    def numSubarraysWithSum_OJ(self, A, S):
        indexes = [-1] + [ix for ix, v in enumerate(A) if v] + [len(A)]
        ans = 0

        if S == 0:
            for i in xrange(len(indexes) - 1):
                # w: number of zeros between two consecutive ones
                w = indexes[i+1] - indexes[i] - 1
                ans += w * (w+1) / 2
            return ans

        for i in xrange(1, len(indexes) - S):
            j = i + S - 1
            left = indexes[i] - indexes[i-1]
            right = indexes[j+1] - indexes[j]
            ans += left * right
        return ans

A, S = [1,0,1,0,1], 1
#A, S = [0, 0, 0, 0], 0
print(Solution().numSubarraysWithSum(A, S))