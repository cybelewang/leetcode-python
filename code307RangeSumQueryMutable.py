"""
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

The update(i, val) function modifies nums by updating the element at index i to val.
Example:
Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8
Note:
The array is only modifiable by the update function.
You may assume the number of calls to update and sumRange function is distributed evenly.
"""
# problem 303's solution: update O(n), query O(1)
# segment tree: update O(logn), query O(logn)
# so we use segment tree. For implementation details, see http://codeforces.com/blog/entry/18051
# Binary Indexed Tree: update O(logn), query O(logn)
# The advantages of Binary Indexed Tree over Segment are, requires less space and very easy to implement..
# Implementation details: http://www.cnblogs.com/grandyang/p/4985506.html
class NumArray_SegmentTree:
    
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        # construct segment tree with size 2*len(nums)
        self.length = len(nums)
        self.st = [0]*self.length
        self.st.extend(nums)

        for i in range(self.length-1, 0, -1): # omit st[0] for easy index calculation
            self.st[i] = self.st[2*i] + self.st[2*i+1]

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        if -1 < i < self.length:
            p = i + self.length
            self.st[p] = val
            while p > 1:
                self.st[p//2] = self.st[p] + self.st[p^1]
                p //= 2

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        res = 0
        if -1 < i <= j < self.length:
            i += self.length
            j += self.length + 1    # make j exclusive
            while i < j:
                if i & 1:
                    res += self.st[i]
                    i += 1
                if j & 1:
                    j -= 1
                    res += self.st[j]
                i //= 2
                j //= 2
        
        return res

class NumArray_BIT: # Binary Indexed Tree
    
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        # construct binary indexed tree with size len(nums) + 1
        self.length = len(nums)
        self.nums = [0]*(self.length)
        self.bit = [0]*(self.length + 1)
        for i in range(self.length):
            self.update(i, nums[i])

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        diff = val - self.nums[i]   # perhaps better to use diff instead of val???
        self.nums[i] = val
        # index in BITree[] is 1 more than the index in arr[]
        i += 1
        # Traverse all ancestors and add 'val'
        while i <= self.length:
            # add val to current node of BI Tree
            self.bit[i] += diff
            # update index to parent
            i += i & (-i)

    def getSum(self, i):
        """
        resturns sum of nums[0...i]
        :type i: int
        """
        res = 0
        # index in BITree[] is 1 more than the index in arr[]
        i += 1
        # Traverse ancestors of BITree[index]
        while i > 0:
            # Add current element of BITree to sum
            res += self.bit[i]
            # Move index to parent node in getSum View
            i -= i & (-i)
        
        return res

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.getSum(j) - self.getSum(i-1)

# Your NumArray object will be instantiated and called as such:
nums = list(range(13))
obj = NumArray_BIT(nums)
print(obj.nums)
print(obj.bit)
print(obj.sumRange(0, 6))
obj.update(0,1)
print(obj.nums)
print(obj.bit)
print(obj.sumRange(0,6))