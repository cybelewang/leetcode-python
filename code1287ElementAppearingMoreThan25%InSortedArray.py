"""
1287 Element Appearing More Than 25% In Sorted Array

Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time.

Return that integer.

Example 1:

Input: arr = [1,2,2,6,6,6,6,7,10]
Output: 6
 
Constraints:

1 <= arr.length <= 10^4
0 <= arr[i] <= 10^5
"""
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        cnt, n = 0, len(arr)
        for i in range(n):
            if i > 0 and arr[i] == arr[i-1]:
                cnt += 1
            else:
                cnt = 1
            if cnt > n/4:
                return arr[i]