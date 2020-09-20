"""
1213 Intersection of Three Sorted Arrays

Given three integer arrays arr1, arr2 and arr3 sorted in strictly increasing order, return a sorted array of only the integers that appeared in all three arrays.

Example 1:

Input: arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]
Output: [1,5]
Explanation: Only 1 and 5 appeared in the three arrays.

Constraints:

1 <= arr1.length, arr2.length, arr3.length <= 1000
1 <= arr1[i], arr2[i], arr3[i] <= 2000
"""
class Solution:
    # a general solution to solve multiple lists, with duplicates
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        iters = [iter(arr1), iter(arr2), iter(arr3)]
        front = [next(it, 0) for it in iters]
        res = []
        while all(front):
            # find the max value of the 3 arrs
            max_val = max(front)
            # iterate all other 2 arrays until their values >= max_val
            for i in range(3):
                while front[i] != 0 and front[i] < max_val:
                    front[i] = next(iters[i], 0)
            # get all same values in 3 iterators
            if front.count(max_val) == 3:
                res.append(max_val)
                for i in range(3):
                    while front[i] != 0 and front[i] == max_val:
                        front[i] = next(iters[i], 0)
        
        return res