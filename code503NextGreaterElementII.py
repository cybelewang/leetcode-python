"""
Given a circular array (the next element of the last element is the first element of the array), print the Next Greater Number for every element. 
The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. 
If it doesn't exist, output -1 for this number.

Example 1:
Input: [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number; 
The second 1's next greater number needs to search circularly, which is also 2.
Note: The length of given array won't exceed 10000.
"""
# similar problems: 496
from collections import deque
class Solution:
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        q = deque()
        # push reversed nums to deque to form a descending order
        for i in range(n-1, -1, -1):
            while q and q[-1][0] <= nums[i]:
                q.pop()
            q.append((nums[i], i))
        
        # similar to problem 496, but need to keep a fixed length windown in deque
        for i in range(n-1, -1, -1):
            # make sure all elements in deque is from a sliding window with length == len(nums)
            if q and q[0][1] == i:
                q.popleft()

            value = nums[i]
            # remove all those elements <= value
            while q and q[-1][0] <= value:
                q.pop()

            nums[i] = -1 if not q else q[-1][0]
            q.append((value, i))
        
        return nums

nums = [1, 2, 1]
print(Solution().nextGreaterElements(nums))