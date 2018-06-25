"""
Given an array nums, we call (i, j) an important reverse pair if i < j and nums[i] > 2*nums[j].

You need to return the number of important reverse pairs in the given array.

Example1:

Input: [1,3,2,3,1]
Output: 2
Example2:

Input: [2,4,3,5,1]
Output: 3
Note:
The length of the given array will not exceed 50,000.
All the numbers in the input array are in the range of 32-bit integer.
"""
from bisect import insort_right, bisect_left, bisect_right
class Solution:
    # BIT based solution, see OneNote for more details
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def BIT_search(bit, i):
            """
            BIT search
            """
            sum_= 0
            while i < len(bit):
                sum_ += bit[i]
                i += i & (-i)
            
            return sum_

        def BIT_insert(bit, i):
            """
            BIT insert
            """
            while i > 0:
                bit[i] += 1
                i -= i & (-i)

        def index(arr, val):
            """
            Find val's index in BIT
            Can we replace this function with bisect_left?
            """
            l, r = 0, len(arr) - 1

            while l <= r:
                m = (l + r)//2
                if arr[m] >= val:
                    r = m - 1
                else:
                    l = m + 1
            
            return l + 1
            
        # main
        res = 0
        copy = nums[:]
        copy.sort()
        bit = [0]*(len(nums)+1)

        for ele in nums:
            res += BIT_search(bit, bisect_left(copy, 2*ele + 1) + 1)
            #res += BIT_search(bit, index(copy, 2*ele + 1))
            BIT_insert(bit, bisect_left(copy, ele) + 1)
            #BIT_insert(bit, index(copy, ele))

        return res


    # TLE
    # my own solution, for each num, find the insertion position of 2*num, and calculate how many numbers in the sorted list are larger than 2*num
    def reversePairs3(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res, sort = 0, []
        for num in nums:
            index = bisect_right(sort, 2*num)
            res += len(sort) - index
            insort_right(sort, num)
        
        return res

nums = [1,3,2,3,1]
obj = Solution()
print(obj.reversePairs(nums))