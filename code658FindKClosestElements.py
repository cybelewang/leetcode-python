"""
658 Find K Closest Elements

Given a sorted array, two integers k and x, find the k closest elements to x in the array. The result should also be sorted in ascending order. 
If there is a tie, the smaller elements are always preferred.

Example 1:
Input: [1,2,3,4,5], k=4, x=3
Output: [1,2,3,4]
Example 2:
Input: [1,2,3,4,5], k=4, x=-1
Output: [1,2,3,4]
Note:
The value k is positive and will always be smaller than the length of the sorted array.
Length of the given array is positive and will not exceed 10^4
Absolute value of elements in the array and x will not exceed 10^4
UPDATE (2017/9/19):
The arr parameter had been changed to an array of integers (instead of a list of integers). Please reload the code definition to get the latest changes.
"""
# similar problems: 719 Find K-th Smallest Pair Distance
# tag: greedy
from bisect import bisect
class Solution:
    # my own solution using binary search and two pointers
    # log(n) + K
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        n = len(arr)
        idx = bisect(arr, x)

        i, j = idx - 1, idx
        for _ in range(k):  # bidirectly expands from idx
            if i < 0:
                j += 1
            elif j > n - 1:
                i -= 1
            else:
                if x - arr[i] > arr[j] - x:
                    j += 1
                else:
                    i -= 1
        
        return arr[i+1:j]

    # 2nd visit on 4/22/2019
    # two pointers and greedy, O(n-k)
    def findClosestElements2(self, arr, k, x):
        i = 0   # start index of the result array
        for j in range(k, len(arr)):
            if abs(arr[j] - x) < abs(arr[i] - x):
                i += 1
            else:
                break
        
        return arr[i:min(i+k, len(arr))]

arr = [1,3,7,9,11]
k = 4
x = 6
print(Solution().findClosestElements2(arr, k, x))