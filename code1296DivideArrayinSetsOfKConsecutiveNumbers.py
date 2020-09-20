"""
1296 Divide Array in Sets of K Consecutive Numbers

Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into sets of k consecutive numbers
Return True if its possible otherwise return False.

Example 1:

Input: nums = [1,2,3,3,4,4,5,6], k = 4
Output: true
Explanation: Array can be divided into [1,2,3,4] and [3,4,5,6].
Example 2:

Input: nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3
Output: true
Explanation: Array can be divided into [1,2,3] , [2,3,4] , [3,4,5] and [9,10,11].
Example 3:

Input: nums = [3,3,2,2,1,1], k = 3
Output: true
Example 4:

Input: nums = [1,2,3,4], k = 3
Output: false
Explanation: Each array should be divided in subarrays of size 3.

Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
1 <= k <= nums.length
Note: This question is the same as 846: https://leetcode.com/problems/hand-of-straights/
"""
from collections import Counter, deque
class Solution:
    # line sweep method, time O(MlogM + N)
    # Use a deque, and push the diff = (current number's count - previously opened straights) into the dequeue
    # When deque size == k, we should remove the most left diff from deque, and decrease opened straights correspondingly
    # Corner cases: 
    # (1) count[cur] < opened, which means current number's count is not enough for required
    # (2) opened > 0 and cur != last + 1, which means current number is not consecutive to last number
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        count = Counter(nums)
        last_checked, opened = -1, 0
        q = deque()
        for i in sorted(count):
            if (opened > 0 and i != last_checked + 1):
                return False
            if count[i] < opened:
                return False
            # below line is unnecessary, but it helps to understand the case len(q) == k
            while q and q[0] == 0: q.popleft()
            # put the diff of opened into queue
            q.append(count[i] - opened)
            opened = count[i] # update the total required opening staights
            # if length of q is k, this means we have enough numbers to form q[0] x straights
            if len(q) == k:
                opened -= q.popleft() # update the total required opening staights
            last_checked = i # update the last checked number
            
        return opened == 0

    # Brutal force solution, time O(MlogM + M*K)
    def isPossibleDivide2(self, nums: List[int], k: int) -> bool:
        count = Counter(nums)
        for num in sorted(count):
            if count[num] == 0:
                continue
            w = count[num]
            for i in range(num, num + k):
                count[i] -= w
                if count[i] < 0:
                    return False
        
        return True