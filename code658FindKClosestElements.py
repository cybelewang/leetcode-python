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
    # wrong solution, can't pass test case [0,0,0,1,3,5,6,7,8,8], k=2, x=2
    def findClosestElements2(self, arr, k, x):
        i = 0   # start index of the result array
        for j in range(k, len(arr)):
            if abs(arr[j] - x) < abs(arr[i] - x):
                i += 1
            else:
                break
        
        return arr[i:min(i+k, len(arr))]

    # time O(n-k), space O(1)
    # solution 1 from https://www.cnblogs.com/grandyang/p/7519466.html
    # greedy method, each time compare the front and back elements' distance to x, and remove the one with larger distance, until the remaining list size is k
    def findClosestElements3(self, arr, k, x):
        i, j = 0, len(arr)-1
        while j - i + 1 > k:
            if abs(arr[j]-x) < abs(arr[i]-x):
                i += 1
            else:
                j -= 1
        
        return arr[i:i+k]

    # best solution O(logN)
    def findClosestElements4(self, arr, k, x):
        left, right = 0, len(arr)-k # len(arr)-k is the most-right possible position, the final result should be <= right
        while left < right:
            mid = (left+right)//2
            if x - arr[mid] > arr[mid+k] - x:
                left = mid + 1
            else:
                right = mid
        
        return arr[left:left+k]

arr = [0,0,0,1,3,5,6,7,8,8]
k = 2
x = 2
print(Solution().findClosestElements4(arr, k, x))