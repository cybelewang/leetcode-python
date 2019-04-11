"""
1013 Partition Array Into Three Parts With Equal Sum

Given an array A of integers, return true if and only if we can partition the array into three non-empty parts with equal sums.
Formally, we can partition the array if we can find indexes i+1 < j with (A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ... + A[j-1] == A[j] + A[j-1] + ... + A[A.length - 1])

Example 1:

Input: [0,2,1,-6,6,-7,9,1,2,0,1]
Output: true
Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
Example 2:

Input: [0,2,1,-6,6,7,9,-1,2,0,1]
Output: false
Example 3:

Input: [3,3,6,5,-2,2,5,1,-9,4]
Output: true
Explanation: 3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4
 
Note:

3 <= A.length <= 50000
-10000 <= A[i] <= 10000
"""
# similar problems: 416 Partition Equal Subset Sum
from collections import defaultdict
class Solution:
    # my own solution by using defaultdict to store the index i of each accumuation A[:i+1]
    def canThreePartsEqualSum(self, A):
        """
        :type A: list[int]
        :rtype: bool
        """
        index, _sum = defaultdict(list), 0
        for i, a in enumerate(A):
            _sum += a
            index[_sum].append(i)
        
        if _sum % 3 != 0:
            return False
        
        _sum = _sum//3
        return len(index[_sum]) > 0 and len(index[2*_sum]) > 0 and min(index[_sum]) < max(index[2*_sum])

# A = [0, 0, 0]   # test if sum is 0, expect True
# A = [1, -1, 0, 1, -1] # test if sum is 0, expect True
# A = [1, -1, 3] # normal test, expect False
A = [1, 3, -2, 4]   # test when 2*_sum appears before _sum, expect False
# A = [0,2,1,-6,6,-7,9,1,2,0,1]   # expect True
# A = [0,2,1,-6,6,7,9,-1,2,0,1]   # expect False
# A = [3,3,6,5,-2,2,5,1,-9,4] # expect True
print(Solution().canThreePartsEqualSum(A))

"""
# O(1) space solution
# https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/discuss/260885/C%2B%2B-6-lines-O(n)-target-sum
bool canThreePartsEqualSum(vector<int>& A, int parts = 0) {
  auto total = accumulate(begin(A), end(A), 0);
  if (total % 3 != 0) return false;
  for (auto i = 0, sum = 0; i < A.size() && parts < (total != 0 ? 2 : 3); ++i) {
    sum += A[i];
    if (sum == total / 3) ++parts, sum = 0;
  }
  return parts == (total != 0 ? 2 : 3);
}
"""